from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

from src.compliance.policy_loader import (
    load_policy
)

from src.compliance.prompts import (
    COMPLIANCE_GAP_PROMPT
)

from src.chains.llm_factory import (
    get_llm
)


class ComplianceService:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

        self.llm = (
            get_llm()
        )

    def analyze(
        self,
        policy_path
    ):

        policy_text = load_policy(
            policy_path
        )

        candidate_docs = (
            self.retriever.retrieve(
                "KYC requirements"
            )
        )

        reranked_docs = (
            self.retriever.rerank(
                "KYC requirements",
                candidate_docs
            )
        )

        docs = [
            doc
            for doc, score
            in reranked_docs
        ]

        regulations = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = (
            COMPLIANCE_GAP_PROMPT
            .format(
                regulations=regulations,
                policy=policy_text
            )
        )

        result = self.llm.invoke(
            prompt
        )

        return result