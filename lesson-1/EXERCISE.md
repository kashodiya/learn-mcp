# Exercise 1: Basic MCP Server and Client

## Objective
Create a basic MCP server with a simple tool and a client that connects to it.

## Step-by-Step Instructions

### Step 1: Set up the project
1. Create a new directory for your lesson
2. Initialize the project with `uv init`
3. Add dependencies to `pyproject.toml`:
   ```toml
   [project]
   dependencies = ["fastmcp"]
   ```
4. Run `uv sync` to install dependencies

### Step 2: Create the MCP Server
1. Create `server.py`
2. Import the FastMCP library
3. Create an MCP instance with a name
4. Define a tool function using the `@mcp.tool()` decorator:
   - Function name: `add`
   - Parameters: `a: int, b: int`
   - Return type: `int`
   - Docstring: "Add two numbers"
   - Implementation: return the sum of a and b
5. Add the main block to run the server:
   - Use SSE transport
   - Host: 127.0.0.1
   - Port: 8000

### Step 3: Create the MCP Client
1. Create `client.py`
2. Import required modules: `Client` from fastmcp, `asyncio`, `pprint`
3. Create an async main function that:
   - Connects to the server at "http://localhost:8000/sse"
   - Lists available tools and prints them
   - Calls the "add" tool with arguments `{"a": 5, "b": 3}`
   - Prints the result using pprint
4. Add the main block to run the async function

### Step 4: Test Your Implementation
1. Start the server: `uv run server.py`
2. In another terminal, run the client: `uv run client.py`
3. Verify the output shows:
   - Available tools list
   - Result of adding 5 + 3 = 8

### Expected Output
The client should display:
- Tool definitions showing the "add" tool
- Result showing the sum calculation

## Key Learning Points
- How to define MCP tools using decorators
- How to run an MCP server with SSE transport
- How to connect a client to an MCP server
- How to list and invoke tools from a client