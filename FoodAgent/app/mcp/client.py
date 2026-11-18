from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


class MCPManager:

    def __init__(self, url):
        self.url = url

    async def connect(self):

        transport = streamablehttp_client(
            self.url
        )

        read, write = await transport.__aenter__()

        session = ClientSession(
            read,
            write
        )

        await session.initialize()

        return session
