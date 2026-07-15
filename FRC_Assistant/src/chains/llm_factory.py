import asyncio

from src.llmservice.CustomLLM_service import CustomLLMService


class CustomLLMLLM:

    def __init__(self):
        self.client = CustomLLMService()

    def invoke(self, prompt: str):

        return asyncio.run(
            self.client.send_prompt(prompt)
        )


def get_llm():

    return CustomLLMLLM()