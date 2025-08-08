
# server.py
import sqlite3
import os
from fastmcp import FastMCP

mcp = FastMCP("SQL Database")

@mcp.tool()
def get_database_schema() -> str:
    """
    Get the complete schema of the chinook database.
    
    Returns:
        str: The complete database schema in markdown format.
    """
    try:
        with open("SCHEMA.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Schema file not found. Please run generate_schema.py first."

@mcp.tool()
def execute_sql(query: str) -> str:
    """
    Execute a SQL query on the chinook database.
    
    Args:
        query (str): The SQL query to execute.
        
    Returns:
        str: The query results formatted as a markdown table.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('chinook.db')
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Check if this is a SELECT query that returns data
        if query.strip().upper().startswith("SELECT"):
            # Get column names
            column_names = [description[0] for description in cursor.description]
            
            # Fetch all rows
            rows = cursor.fetchall()
            
            # Format as markdown table
            result = "| " + " | ".join(column_names) + " |\n"
            result += "|" + "|".join(["---" for _ in column_names]) + "|\n"
            
            # Add data rows
            for row in rows:
                result += "| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |\n"
            
            # Close connection
            conn.close()
            
            return result
        else:
            # For non-SELECT queries, return the number of affected rows
            affected_rows = cursor.rowcount
            conn.commit()
            conn.close()
            
            return f"Query executed successfully. Affected rows: {affected_rows}"
    
    except sqlite3.Error as e:
        # Handle any database errors
        return f"Error executing SQL query: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=50873)
