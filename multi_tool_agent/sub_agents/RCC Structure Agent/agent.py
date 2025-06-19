from google.adk import Agent
from vertexai import rag
from . import prompt

MODEL = "gemini-2.0-flash"

def rag_response(query:str) -> str:
    """
    Retrieves contextually relevant information from a RAG corpus.

    Args:
        query (str): The query string to search within the corpus.

    Returns:
        vertexai.rag.RagRetrievalQueryResponse: The response containing retrieved
        information from the corpus.
    """
    corpus_name = "projects/engineer-code-consultant/locations/us-east4/ragCorpora/6917529027641081856"

    response = rag.retrieval_query(
            rag_resources=[
                rag.RagResource(
                    rag_corpus=corpus_name,
                    )
                ],
            text=query,
            )

    return str(response)

root_agent = Agent(
        model=MODEL,
        name="RCC_Structures_Agent_prompt",
        instruction=prompt.RCC_STRUCTURE_AGENT_PROMPT,
        tools=[rag_response]
        )
