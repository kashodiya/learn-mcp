

import asyncio
import pprint
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_aws import ChatBedrock

async def main():
    llm = ChatBedrock(model="us.anthropic.claude-3-7-sonnet-20250219-v1:0")

    client = MultiServerMCPClient(
        {
            "sql_database": {
                "url": "http://localhost:50873/sse",
                "transport": "sse",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    
    # Example query to demonstrate the agent using the SQL tools
    query = "What are the top 5 artists with the most albums in the database?"
    
    print(f"Asking the agent: {query}")
    response = await agent.ainvoke({"messages": query})

    pprint.pprint(response)

if __name__ == "__main__":
    asyncio.run(main())

