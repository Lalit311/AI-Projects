import asyncio
from graph.state import GraphState
from prompts.system_prompt import SYSTEM_PROMPT
from prompts.response_prompt import RESPONSE_PROMPT
from services.custom_llm_service import CustomLLMService
from backend.utils.logger import logger


def response_node(state: GraphState):
    logger.info("Generating final response")

    prompt = RESPONSE_PROMPT.format(
        question=state.question,
        tool_outputs=state.tool_outputs
    )
    
    llm_service = CustomLLMService()
    response = asyncio.run(llm_service.send_prompt(system_prompt=SYSTEM_PROMPT, user_prompt=prompt))

    return {
        "final_answer": response
    }