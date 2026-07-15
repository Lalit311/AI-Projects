from src.retrieval.bm25_retriever import (
    get_bm25_retriever
)

from src.retrieval.retriever import (
    retriever as vector_retriever
)

from src.retrieval.reranker import (
    Reranker
)


class HybridRetriever:

    def __init__(self):

        self.bm25 = get_bm25_retriever()

        self.vector = vector_retriever

        self.reranker = Reranker()

    def retrieve(
        self,
        query
    ):

        bm25_docs = self.bm25.invoke(
            query
        )

        vector_docs = self.vector.invoke(
            query
        )

        combined = []

        seen = set()

        for doc in (
            bm25_docs +
            vector_docs
        ):

            key = (
                doc.metadata["source_file"],
                doc.metadata["page"]
            )

            if key in seen:
                continue

            seen.add(key)

            combined.append(doc)

        return combined

    def rerank(
        self,
        query,
        docs
    ):

        return self.reranker.rerank(
            query,
            docs,
            top_k=5
        )