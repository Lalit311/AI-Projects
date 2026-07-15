from src.vectorstore.chroma_store import load_vectorstore


vectorstore = load_vectorstore()

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)