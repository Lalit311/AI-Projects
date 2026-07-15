from langchain_core.runnables import Runnable
from src.chains.llm_factory import get_llm

class CustomLLMRunnable(Runnable):

    def invoke(self, input, config=None):
        llm = get_llm()
        return llm.invoke(input)