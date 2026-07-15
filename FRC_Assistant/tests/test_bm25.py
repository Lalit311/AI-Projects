from src.retrieval.bm25_retriever import (
    get_bm25_retriever
)

retriever = get_bm25_retriever()

docs = retriever.invoke(
    "CKYCR"
)

for doc in docs:

    print(
        doc.metadata["source_file"]
    )

    print(
        doc.page_content[:300]
    )

    print("=" * 80)