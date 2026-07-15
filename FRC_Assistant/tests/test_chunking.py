from src.ingestion.load_docs import load_documents
from src.ingestion.chunker import create_chunks

docs = []

docs.extend(load_documents("data/rbi"))
docs.extend(load_documents("data/sebi"))

print(f"\nPages Loaded: {len(docs)}")

chunks = create_chunks(docs)

print(f"\nChunks Created: {len(chunks)}")

print("\nSample Metadata:")
print(chunks[0].metadata)

print("\nChunk Length:")
print(len(chunks[0].page_content))

print("\nSample Chunk:")
print(chunks[0].page_content[:1000])