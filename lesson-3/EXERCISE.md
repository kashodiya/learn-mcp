# Exercise 3: SQL Database Integration with MCP

## Objective
Create an MCP server that provides AI agents access to a SQLite database through SQL query tools.

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
       "langchain-aws",
       "fastapi",
       "uvicorn"
   ]
   ```
3. Run `uv sync` to install dependencies
4. Ensure you have the `chinook.db` SQLite database file in your project directory

### Step 2: Generate Database Schema
1. Create `generate_schema.py` to extract database schema information
2. Connect to `chinook.db` using sqlite3
3. Extract table definitions, columns, and sample data
4. Generate a `SCHEMA.md` file with the database structure in markdown format
5. Run the script to create the schema file

### Step 3: Create the SQL MCP Server
1. Create `server.py`
2. Import required modules: `sqlite3`, `os`, `FastMCP`
3. Create FastMCP instance named "SQL Database"
4. Define two tools:

   **Tool 1: `get_database_schema() -> str`**
   - Read and return contents of `SCHEMA.md`
   - Handle FileNotFoundError with appropriate message

   **Tool 2: `execute_sql(query: str) -> str`**
   - Print the SQL query for debugging
   - Connect to `chinook.db`
   - Execute the query
   - For SELECT queries: format results as markdown table
   - For other queries: return affected row count
   - Handle sqlite3.Error exceptions

5. Run server on port 50873 with SSE transport

### Step 4: Create the AI Agent Client
1. Create `client.py`
2. Set up ChatBedrock LLM and MultiServerMCPClient
3. Configure client to connect to "http://localhost:50873/sse"
4. Create React agent with LLM and MCP tools
5. Ask the agent: "What are the top 5 artists with the most albums in the database?"
6. Print the agent's final response

### Step 5: Create Web Interface (Optional)
1. Create `app.py` with FastAPI
2. Add endpoint `/ask` that accepts questions and returns AI responses
3. Create `static/index.html` with a simple web form
4. Test the web interface at http://localhost:8000

### Step 6: Test Your Implementation
1. Generate schema: `python generate_schema.py`
2. Start MCP server: `python server.py`
3. Test with client: `python client.py`
4. Optionally test web app: `uv run uvicorn app:app --reload`

### Expected Behavior
The AI agent should:
1. First call `get_database_schema` to understand the database structure
2. Analyze the schema to identify relevant tables (Artist, Album)
3. Generate appropriate SQL query (JOIN Artist and Album tables, GROUP BY, ORDER BY)
4. Call `execute_sql` with the generated query
5. Interpret results and provide a natural language answer

### Sample SQL Query
The agent should generate something like:
```sql
SELECT a.Name, COUNT(al.AlbumId) as album_count 
FROM Artist a 
JOIN Album al ON a.ArtistId = al.ArtistId 
GROUP BY a.ArtistId, a.Name 
ORDER BY album_count DESC 
LIMIT 5
```

## Key Learning Points
- How to integrate MCP with databases
- How to provide schema information to AI agents
- How to handle SQL query execution and error handling
- How AI agents can reason about database structures
- How to format database results for AI consumption
- Building web interfaces for MCP-powered applications