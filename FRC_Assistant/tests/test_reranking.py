from src.retrieval.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

while True:

    query = input(
        "\nEnter Query (or 'exit'): "
    )

    if query.lower() == "exit":
        break

    results = retriever.invoke(query)

    print("\n" + "=" * 120)
    print("RERANKED RESULTS")
    print("=" * 120)

    for idx, (doc, score) in enumerate(
        results,
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

        print("\nContent Preview:\n")

        print(
            doc.page_content[:500]
        )

        print(
            "\n" + "-" * 120
        )