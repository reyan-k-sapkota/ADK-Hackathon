from google.adk.agents import Agent

import fitz  # PyMuPDF
import requests
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load the embedding model once
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def get_pdf_url_for_country(country: str) -> str:
    urls = {
        "nepal": "https://giwmscdnone.gov.np/media/pdf_upload/NBC_205_READY-TO-USE_DETAILING_GUIDELINE_FOR-signed.pdf",
        "india": "https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf",
    }
    return urls.get(country.lower(), "")


def download_and_extract_pdf(url: str) -> list[tuple[int, str]]:
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)

    doc = fitz.open("temp.pdf")
    return [(i + 1, page.get_text()) for i, page in enumerate(doc)]


def create_chunks(pages, chunk_size=500) -> list[tuple[int, str]]:
    chunks = []
    for page_num, text in pages:
        sentences = text.split(". ")
        chunk = ""
        for sentence in sentences:
            if len(chunk) + len(sentence) < chunk_size:
                chunk += sentence + ". "
            else:
                chunks.append((page_num, chunk.strip()))
                chunk = sentence + ". "
        if chunk:
            chunks.append((page_num, chunk.strip()))
    return chunks


def embed_chunks(chunks):
    texts = [c[1] for c in chunks]
    embeddings = embedder.encode(texts)
    return np.array(embeddings), texts, [c[0] for c in chunks]


def store_embeddings(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def search(index, query, texts, page_nums, k=5):
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding), k)
    return [(texts[i], page_nums[i]) for i in I[0]]


def get_code_snippets(query: str, country: str) -> str:
    """
    Returns relevant code of practice excerpts for a given engineering query and country.
    """
    url = get_pdf_url_for_country(country)
    if not url:
        return f"No code available for country: {country}"

    pages = download_and_extract_pdf(url)
    chunks = create_chunks(pages)
    embeddings, texts, page_nums = embed_chunks(chunks)
    index = store_embeddings(embeddings)

    results = search(index, query, texts, page_nums)

    output = []
    for text, page in results:
        output.append(f"📄 Page {page}:\n{text}")
    return "\n\n".join(output)


# Define the agent
root_agent = Agent(
    name="engineering_code_consultant",
    model="gemini-2.0-flash",
    description="Provides region-specific consultation based on national engineering codes.",
    instruction=(
        "You are an engineering consultant AI that answers structural or civil engineering questions "
        "using national codes of practice. Use the `get_code_snippets` tool to retrieve relevant sections "
        "from the code document and cite page numbers when giving your answer."
    ),
    tools=[get_code_snippets],
)

