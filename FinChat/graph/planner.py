import asyncio
from google import genai
from config import MODEL_NAME
from graph.state import GraphState
from prompts.planner_prompt import PLANNER_PROMPT
from backend.utils.json_parser import parse_json
from services.custom_llm_service import CustomLLMService
from backend.utils.logger import logger


def planner_node(state: GraphState):
    logger.info("Planner started")
    
    prompt = f"""
        User Question:
        {state.question}
    """

    llm_service = CustomLLMService()
    result = asyncio.run(llm_service.send_prompt(system_prompt=PLANNER_PROMPT, user_prompt=prompt))
    print(result)
    # result = parse_json(asyncio.run(llm_service.send_prompt(prompt)))

    return {
        "intent": result["intent"],
        "execution_plan": result["execution_plan"]
    }