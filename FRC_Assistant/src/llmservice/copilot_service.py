import asyncio

from copilot import CopilotClient
from copilot.session import PermissionHandler


class CopilotService:

    def __init__(self, model: str):
        self.model = model
        self.client = None
        self.session = None

    async def connect(self):
        client = CopilotClient()
        await client.start()

        session = await client.create_session(
            on_permission_request=PermissionHandler.approve_all,
            model=self.model
        )
        
        self.client = client
        self.session = session

    async def close(self):
        if self.session:
            await self.session.destroy()

        if self.client:
            await self.client.stop()

    async def send_prompt(self, prompt: str) -> str:
        done = asyncio.Event()
        response_chunks = []

        def on_event(event):
            if event.type.value == "assistant.message":
                response_chunks.append(event.data.content)

            elif event.type.value == "session.idle":
                done.set()

        self.session.on(on_event)

        await self.session.send({
            "prompt": prompt
        })

        await done.wait()

        return "".join(response_chunks)