from fastmcp import Client
import asyncio
import pprint

async def main():
    async with Client("http://localhost:8000/sse") as client:
        tools = await client.list_tools()
        print("Available tools:")
        print(tools)
        print('\nCalling tool: ("add", {"a": 5, "b": 3})')
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print("\nResult:")
        pprint.pprint(result)

if __name__ == "__main__":
    asyncio.run(main())