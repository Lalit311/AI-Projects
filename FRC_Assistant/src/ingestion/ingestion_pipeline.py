from src.ingestion.load_docs import load_documents
from src.ingestion.chunker import create_chunks

from src.vectorstore.create_db import create_vectorstore

def run_ingestion():
    docs = []

    docs.extend(load_documents("data/rbi"))
    docs.extend(load_documents("data/sebi"))
    print(f"Pages Loaded: {len(docs)}")

    chunks = create_chunks(docs)
    print(f"Chunks Created: {len(chunks)}")

    vectorstore = create_vectorstore(chunks)
    print("Vector Store Created Successfully")
    
    return len(chunks)