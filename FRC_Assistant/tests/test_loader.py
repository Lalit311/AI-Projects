from src.ingestion.load_docs import load_documents

docs = load_documents("data/sebi")

print(f"\nTotal Pages Loaded: {len(docs)}")

print("\nSample Metadata:")

print(docs[0].metadata)

print("\nSample Text:\n")

print(docs[0].page_content[:1000])