from src.retrieval.retriever import get_retriever
from src.chains.llm_factory import get_llm
from src.chains.prompts import RAG_PROMPT

from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from src.retrieval.retriever import (
    get_retriever
)

from src.chains.prompts import (
    RAG_PROMPT
)

from src.chains.helpers import (
    format_docs,
    prompt_to_string
)

from src.chains.custom_llm_runnable import (
    CustomLLMRunnable
)


retriever = get_retriever()


rag_chain = (
    {
        "context":
            retriever
            | RunnableLambda(format_docs),

        "question":
            RunnablePassthrough()
    }
    | RAG_PROMPT
    | RunnableLambda(prompt_to_string)
    | CustomLLMRunnable()
    # | StrOutputParser()
)


def build_sources(docs):

    seen = set()
    sources = []

    for doc in docs:
        source_key = (
            doc.metadata["source_file"],
            doc.metadata["page"]
        )

        if source_key in seen:
            continue

        seen.add(source_key)

        sources.append(
            {
                "document":
                    doc.metadata["source_file"],
                "page":
                    doc.metadata["page"]
            }
        )

    return sources


def ask_question(
    question: str
):

    retriever = get_retriever()

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm = get_llm()

    answer = llm.invoke(
        prompt
    )

    return {
        "answer": answer,
        "sources": build_sources(docs)
    }