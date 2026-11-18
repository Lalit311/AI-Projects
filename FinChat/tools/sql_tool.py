import asyncio
from datetime import date
from prompts.system_prompt import SYSTEM_PROMPT
from prompts.sql_prompt import SQL_PROMPT
from backend.utils.db import execute_query
from backend.utils.sql_utils import clean_sql
from services.custom_llm_service import CustomLLMService
from backend.utils.logger import logger


class SQLTool:

    def run(self, question: str):
        logger.info("Executing SQL Tool")

        prompt = SQL_PROMPT.format(
            today=date.today(),
            question=question
        )

        llm_service = CustomLLMService()
        response = asyncio.run(llm_service.send_prompt(system_prompt=SYSTEM_PROMPT, user_prompt=prompt))

        sql = clean_sql(response)
        rows = execute_query(sql)

        return {
            "generated_sql": sql,
            "rows": rows
        }