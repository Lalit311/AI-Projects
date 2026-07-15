from langchain_community.retrievers import BM25Retriever

from src.ingestion.load_docs import (
    load_documents
)

from src.ingestion.chunker import (
    create_chunks
)


def get_bm25_retriever():

    docs = []

    docs.extend(
        load_documents("data/rbi")
    )

    docs.extend(
        load_documents("data/sebi")
    )

    chunks = create_chunks(docs)

    retriever = BM25Retriever.from_documents(
        chunks
    )

    retriever.k = 5

    return retriever