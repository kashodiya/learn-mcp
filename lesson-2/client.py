import asyncio
import pprint
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_aws import ChatBedrock

async def main():
    llm = ChatBedrock(model="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

    client = MultiServerMCPClient(
        {
            "math": {
                # Make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})

    pprint.pprint(math_response)

if __name__ == "__main__":
    asyncio.run(main())
