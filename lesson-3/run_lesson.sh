
#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
uv sync

# Generate schema if it doesn't exist
if [ ! -f "SCHEMA.md" ]; then
    echo "Generating database schema..."
    python generate_schema.py
fi

# Start the server in the background
echo "Starting MCP server..."
python server.py > server.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
echo "Waiting for server to start..."
sleep 3

# Run the test script
echo "Running test script to verify server functionality..."
python test_server.py

echo ""
echo "To run the AI agent client, open a new terminal and run:"
echo "python client.py"

echo ""
echo "Press Ctrl+C to stop the server"

# Wait for Ctrl+C
wait $SERVER_PID
