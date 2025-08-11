# Exercise 4: An agent which remembers past conversations

## Objective
Create a basic MCP agent with multiple agents that has memory

## Plan
- We will use a MCP agent framework called mcp-agent so that we do not need to write boilerplate code for managing session, memory etc. 
- You can read more about that framework here: https://github.com/lastmile-ai/mcp-agent


## Learning
- Review main.py how it is using mcp_agent.
- MCP servers are configured in mcp_agent.config.yaml
- We are asking the agent to count customers.
- To check memory we are asking:
    - What was the previous question.
    - What SQL was used.


## Prepare
- Copy mcp_agent.secrets.yaml.example to mcp_agent.secrets.yaml
- Fill in aws_access_key_id, aws_secret_access_key, and aws_session_token. If you are using AWS profile, you do not need to add these values. 
- Install dependencies
```bash
uv sync
```
- Run agent
```bash
uv run client.py
```
