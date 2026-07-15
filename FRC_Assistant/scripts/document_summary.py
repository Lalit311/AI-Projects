from collections import Counter

from src.ingestion.load_docs import load_documents

docs = load_documents("data/sebi")

files = [d.metadata["source_file"] for d in docs]

counter = Counter(files)

print("\nPages Per Document\n")

for file_name, count in counter.items():
    print(f"{file_name}: {count}")