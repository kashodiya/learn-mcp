

import asyncio
from fastmcp import Client

async def main():
    # Connect to the MCP server
    async with Client("http://localhost:50873/sse") as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:")
        print(tools)
        
        # Test get_database_schema tool
        print("\nTesting get_database_schema tool:")
        schema = await client.call_tool("get_database_schema", {})
        # Print just the first 500 characters to avoid flooding the console
        print(schema[:500] + "...\n(truncated)")
        
        # Test execute_sql tool with a simple query
        print("\nTesting execute_sql tool:")
        query = "SELECT ArtistId, Name FROM Artist LIMIT 5;"
        result = await client.call_tool("execute_sql", {"query": query})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

