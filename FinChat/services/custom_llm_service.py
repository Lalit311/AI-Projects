import asyncio
import time
import httpx

from config import settings


class CustomLLMService:

    POLL_INTERVAL = 5
    TIMEOUT = 600

    @staticmethod
    def headers():

        return {
            "Authorization":
                f"Bearer {settings.WORKFLOW_PAT_TOKEN}",
            "Content-Type":
                "application/json",
            "X-Trace-User-ID":
                f"FRC_Assistant-{int(time.time())}"
        }

    async def start_run(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        url = (
            f"{settings.WORKFLOW_BASE_URL}"
            f"/api/v1/tasks/"
            f"{settings.WORKFLOW_TASK_ID}/runs"
        )

        payload = {
            "runName":
                f"FRC_Assistant-{int(time.time())}",
            "overrides": {
                "workflow":
                    settings.WORKFLOW_ID,
                "variables": {
                    "System_Prompt": system_prompt,
                    "User_Prompt": user_prompt
                }
            }
        }

        async with httpx.AsyncClient() as client:

            response = await client.post(
                url,
                json=payload,
                headers=self.headers(),
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            return data["id"]

    async def poll(
        self,
        run_id: str
    ):

        url = (
            f"{settings.WORKFLOW_BASE_URL}"
            f"/api/v1/tasks/"
            f"{settings.WORKFLOW_TASK_ID}"
            f"/runs/{run_id}"
        )

        start_time = time.time()

        async with httpx.AsyncClient() as client:

            while (
                time.time() - start_time
                < self.TIMEOUT
            ):

                response = await client.get(
                    url,
                    headers=self.headers(),
                    timeout=30
                )

                response.raise_for_status()

                data = response.json()

                status = (
                    data.get(
                        "status",
                        ""
                    ).lower()
                )

                if status in (
                    "completed",
                    "success"
                ):
                    return data

                if status in (
                    "failed",
                    "error"
                ):
                    raise RuntimeError(
                        f"Workflow failed: {status}"
                    )

                await asyncio.sleep(
                    self.POLL_INTERVAL
                )

        raise TimeoutError(
            "Workflow timed out"
        )

    def extract_response(
        self,
        result
    ):

        outputs = result.get(
            "exec_metadata",
            {}
        ).get(
            "allOutputs",
            {}
        )

        for node_name, node_output in outputs.items():

            try:

                llm_response = (
                    node_output["LLM"]["data"]["response"]
                )

                if llm_response:

                    return llm_response

            except (
                KeyError,
                TypeError
            ):
                continue

        raise ValueError(
            "No LLM response found in workflow output."
        )

    async def send_prompt(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        run_id = await self.start_run(
            system_prompt,
            user_prompt
        )

        result = await self.poll(
            run_id
        )

        # return self.extract_response(
        #     result
        # )
        
        return next(v['LLM for RAG']['data']['result']['response'] for k, v in result['exec_metadata']['allOutputs'].items() if k.startswith('FRC_Assistant'))