
import sqlite3
import os

def generate_schema_markdown():
    """Generate a markdown file with the complete schema of the chinook.db"""
    
    # Connect to the database
    conn = sqlite3.connect('chinook.db')
    cursor = conn.cursor()
    
    # Get list of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = cursor.fetchall()
    
    # Create markdown content
    markdown = "# Chinook Database Schema\n\n"
    markdown += "This document describes the schema of the Chinook SQLite database.\n\n"
    
    # For each table, get its schema and sample data
    for table in tables:
        table_name = table[0]
        markdown += f"## {table_name}\n\n"
        
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        # Create table schema section
        markdown += "### Schema\n\n"
        markdown += "| Column | Type | Not Null | Primary Key | Default |\n"
        markdown += "|--------|------|----------|-------------|--------|\n"
        
        for col in columns:
            col_id, name, type_, not_null, default_val, pk = col
            markdown += f"| {name} | {type_} | {bool(not_null)} | {bool(pk)} | {default_val if default_val is not None else ''} |\n"
        
        # Get foreign keys
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        foreign_keys = cursor.fetchall()
        
        if foreign_keys:
            markdown += "\n### Foreign Keys\n\n"
            markdown += "| Column | References | On Delete | On Update |\n"
            markdown += "|--------|------------|-----------|----------|\n"
            
            for fk in foreign_keys:
                id_, seq, table, from_, to, on_update, on_delete, match = fk
                markdown += f"| {from_} | {table}({to}) | {on_delete} | {on_update} |\n"
        
        # Get sample data (first 5 rows)
        try:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            sample_data = cursor.fetchall()
            
            if sample_data:
                markdown += "\n### Sample Data\n\n"
                
                # Get column names for the header
                column_names = [description[0] for description in cursor.description]
                
                # Create the header row
                markdown += "| " + " | ".join(column_names) + " |\n"
                markdown += "|" + "|".join(["---" for _ in column_names]) + "|\n"
                
                # Add the data rows
                for row in sample_data:
                    markdown += "| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |\n"
        except sqlite3.OperationalError:
            # Some tables might not support direct SELECT
            markdown += "\n*Sample data not available for this table.*\n"
        
        markdown += "\n\n"
    
    # Close the connection
    conn.close()
    
    # Write to file
    with open("SCHEMA.md", "w") as f:
        f.write(markdown)
    
    print("Schema documentation generated in SCHEMA.md")

if __name__ == "__main__":
    generate_schema_markdown()
