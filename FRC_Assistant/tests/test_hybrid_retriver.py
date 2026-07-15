from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

retriever = HybridRetriever()

docs = retriever.invoke(
    "customer identification requirements"
)

for doc in docs:

    print(
        doc.metadata["source_file"]
    )

    print(
        doc.metadata["page"]
    )

    print("=" * 50)