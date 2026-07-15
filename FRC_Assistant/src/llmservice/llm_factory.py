from core.config import settings

from src.llmservice.copilot_service import (
    CopilotService
)

from src.llmservice.CustomLLM_service import (
    CustomLLMService
)

class LLMFactory:

    @staticmethod
    def get_service():

        provider = (
            settings.LLM_PROVIDER
            .upper()
        )

        if provider == "COPILOT":

            return CopilotService(
                model=settings.MODEL
            )

        if provider == "CustomLLM":

            return CustomLLMService()

        raise ValueError(
            f"Unsupported provider: "
            f"{provider}"
        )