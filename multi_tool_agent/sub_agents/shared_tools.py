from vertexai import rag

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
