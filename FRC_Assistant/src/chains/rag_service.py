from src.retrieval.retriever import (
    retriever
)

from src.chains.helpers import (
    format_docs,
    prompt_to_string
)

from src.chains.prompts import (
    RAG_PROMPT
)

from src.chains.llm_factory import (
    get_llm
)


class RAGService:

    def __init__(self):

        self.retriever = (
            retriever
        )

        self.llm = get_llm()

    def ask(
        self,
        question
    ):

        docs = self.retriever.invoke(
            question
        )

        context = format_docs(
            docs
        )

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question
            }
        )

        answer = self.llm.invoke(
            prompt_to_string(
                prompt
            )
        )

        sources = []

        seen = set()

        for doc in docs:

            key = (
                doc.metadata[
                    "source_file"
                ],
                doc.metadata[
                    "page"
                ]
            )

            if key in seen:
                continue

            seen.add(key)

            sources.append(
                {
                    "document":
                        doc.metadata[
                            "source_file"
                        ],
                    "page":
                        doc.metadata[
                            "page"
                        ]
                }
            )

        return {
            "answer": answer,
            "sources": sources
        }