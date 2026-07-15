from langchain_community.vectorstores import Chroma
from src.vectorstore.embedder import (
    get_embeddings
)


PERSIST_DIR = "./chroma_db"


def create_vectorstore(documents):

    return Chroma.from_documents(
        documents=documents,
        embedding=get_embeddings(),
        persist_directory=PERSIST_DIR
    )


def load_vectorstore():

    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embeddings()
    )