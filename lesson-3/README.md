

# Lesson 3: SQL Database with MCP

In this lesson, we'll create an MCP server that can interact with a SQLite database. The server will expose tools that allow an AI agent to:

1. Get the database schema
2. Execute SQL queries against the database

This demonstrates how MCP can be used to give AI agents access to structured data through SQL.

## Database

We're using the Chinook SQLite database, which represents a digital media store with tables for artists, albums, tracks, invoices, and customers.

## Files in this Lesson

- `chinook.db`: The SQLite database file
- `generate_schema.py`: Script to generate a markdown file with the database schema
- `SCHEMA.md`: Generated file containing the database schema
- `server.py`: MCP server that exposes tools for database interaction
- `client.py`: Client that connects to the MCP server and uses an AI agent to query the database

## Key Concepts

### 1. Database Schema Generation

The `generate_schema.py` script connects to the SQLite database and extracts:
- Table definitions
- Column information
- Foreign key relationships
- Sample data

This information is formatted as markdown and saved to `SCHEMA.md`.

### 2. MCP Tools for Database Interaction

The server exposes two tools:

- `get_database_schema()`: Returns the complete database schema from the SCHEMA.md file
- `execute_sql(query)`: Executes a SQL query against the database and returns the results

### 3. AI Agent Integration

The client demonstrates how to:
- Connect to the MCP server
- Get the available tools
- Create an AI agent with access to these tools
- Ask the agent to solve a problem that requires SQL knowledge

## How to Run

1. Install dependencies
```bash
uv sync
```

2. Generate the database schema (already done, but you can re-run if needed)
```bash
python generate_schema.py
```

3. Start the MCP server
```bash
python server.py
```

4. In a new terminal, run the client
```bash
python client.py
```

## Expected Output

When you run the client, you should see the AI agent:
1. Understand the query
2. First use the `get_database_schema` tool to understand the database structure
3. Formulate an appropriate SQL query
4. Use the `execute_sql` tool to run the query
5. Interpret the results and provide an answer

## Exercise Ideas

1. Modify the client to ask different questions about the database
2. Add a new tool to the server that provides query suggestions
3. Extend the schema generation to include indexes and views

