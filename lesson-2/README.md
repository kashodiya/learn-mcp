# Exercise 2: MCP with AI Agent Integration

## Objective
Create an MCP server with multiple math tools and integrate it with an AI agent using LangChain.

## Step-by-Step Instructions

### Step 1: Set up the project
1. Initialize the project with `uv init`
2. Add dependencies to `pyproject.toml`:
   ```toml
   [project]
   dependencies = [
       "fastmcp",
       "langchain-mcp-adapters",
       "langgraph",
       "langchain-aws"
   ]
   ```
3. Run `uv sync` to install dependencies

### Step 2: Create the Math MCP Server
1. Create `server.py`
2. Import FastMCP and create an instance named "Math"
3. Define two tools using `@mcp.tool()` decorator:
   - `add(a: int, b: int) -> int`: Add two numbers
   - `multiply(a: int, b: int) -> int`: Multiply two numbers
4. Run the server on port 8000 with SSE transport

### Step 3: Create the AI Agent Client
1. Create `client.py`
2. Import required modules:
   - `asyncio`, `pprint`
   - `MultiServerMCPClient` from langchain_mcp_adapters.client
   - `create_react_agent` from langgraph.prebuilt
   - `ChatBedrock` from langchain_aws
3. Create an async main function that:
   - Initializes ChatBedrock with model "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
   - Creates MultiServerMCPClient with server config:
     ```python
     {
         "math": {
             "url": "http://localhost:8000/sse",
             "transport": "sse",
         }
     }
     ```
   - Gets tools from the client
   - Creates a React agent with the LLM and tools
   - Asks the agent: "what's (3 + 5) x 12?"
   - Prints the response using pprint

### Step 4: Test Your Implementation
1. Ensure AWS credentials are configured
2. Start the server: `uv run server.py`
3. In another terminal, run the client: `uv run client.py`
4. Observe how the AI agent:
   - First calls the `add` tool with (3, 5)
   - Then calls the `multiply` tool with (8, 12)
   - Provides the final answer: 96

### Expected Behavior
The AI agent should:
1. Break down the problem into steps
2. Use the `add` tool to calculate (3 + 5) = 8
3. Use the `multiply` tool to calculate 8 × 12 = 96
4. Provide a natural language response with the answer

## Key Learning Points
- How to create multiple tools in an MCP server
- How to integrate MCP with LangChain adapters
- How to create AI agents that can use MCP tools
- How AI agents reason about which tools to use and when


## How to run the solution from this folder?
- Install dependencies
```bash
uv sync
```

- Start server
```bash
uv run server.py
```

- Run client
```bash
uv run client.py
```