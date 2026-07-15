from src.ingestion.load_docs import load_documents
from src.ingestion.chunker import create_chunks

docs = []

docs.extend(load_documents("data/rbi"))
docs.extend(load_documents("data/sebi"))

chunks = create_chunks(docs)

sizes = [len(chunk.page_content) for chunk in chunks]

print(f"Total Chunks: {len(chunks)}")
print(f"Min Size: {min(sizes)}")
print(f"Max Size: {max(sizes)}")
print(f"Average Size: {sum(sizes)/len(sizes):.2f}")