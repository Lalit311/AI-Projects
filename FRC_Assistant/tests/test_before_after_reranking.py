from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

retriever = HybridRetriever()

query = input(
    "Enter Query: "
)

candidate_docs = retriever.retrieve(
    query
)

print(
    "\n" + "=" * 100
)

print(
    "BEFORE RERANKING"
)

print(
    "=" * 100
)

for idx, doc in enumerate(
    candidate_docs,
    start=1
):

    print(
        f"\nRank #{idx}"
    )

    print(
        f"Document: "
        f"{doc.metadata['source_file']}"
    )

    print(
        f"Page: "
        f"{doc.metadata['page']}"
    )

    print(
        doc.page_content[:250]
    )

print(
    "\n" + "=" * 100
)

print(
    "AFTER RERANKING"
)

print(
    "=" * 100
)

reranked_docs = retriever.rerank(
    query,
    candidate_docs
)

for idx, (
    doc,
    score
) in enumerate(
    reranked_docs,
    start=1
):

    print(
        f"\nRank #{idx}"
    )

    print(
        f"Score: {score:.4f}"
    )

    print(
        f"Document: "
        f"{doc.metadata['source_file']}"
    )

    print(
        f"Page: "
        f"{doc.metadata['page']}"
    )

    print(
        doc.page_content[:250]
    )