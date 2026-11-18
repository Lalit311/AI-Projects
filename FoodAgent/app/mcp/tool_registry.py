async def get_tools(session):

    tools = await session.list_tools()

    converted = []

    for tool in tools.tools:

        converted.append(
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            }
        )

    return converted
