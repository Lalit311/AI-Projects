from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def score(
        self,
        query,
        docs
    ):

        pairs = [
            (query, doc.page_content)
            for doc in docs
        ]

        scores = self.model.predict(
            pairs
        )

        return scores

    def rerank(
        self,
        query,
        docs,
        top_k=5
    ):

        scores = self.score(
            query,
            docs
        )

        ranked = sorted(
            zip(docs, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]