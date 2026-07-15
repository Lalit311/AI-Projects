from src.retrieval.retriever import get_retriever

retriever = get_retriever()

query = "What are KYC requirements for customer identification?"

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} chunks\n")

for i, doc in enumerate(results):
    print("=" * 80)
    print(f"Result {i+1}")
    print(doc.metadata)
    print()
    print(doc.page_content[:500])