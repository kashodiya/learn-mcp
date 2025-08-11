# Learning MCP
Learn Model Context Protocol (MCP) through hands-on examples.


### What You'll Learn
- **Lesson 1: Manual Tool Definition and Execution**
  - How to define MCP tools and call them manually
  - Understanding the basic structure of MCP tools

- **Lesson 2: LLM-Driven Tool Selection**
  - How to integrate with Large Language Models (LLMs)
  - Enabling LLMs to automatically select and execute appropriate tools

- **Lesson 3: Web Integration and Database Connectivity**
  - How to expose MCP functionality through web applications
  - Connecting MCP servers to backend systems and databases
  - Building user-facing interfaces for MCP tools

### Learning Path
1. **Prepare your environment**: See section below.
2. **Follow the Sequential Order**: Start with Lesson 1, then progress through Lessons 2 and 3
3. **Read First, Code Second**: Each lesson includes a comprehensive README.md with detailed instructions
4. **Complete Examples Provided**: Every lesson folder contains fully functional code examples
5. **Multiple Learning Approaches**:
   - **Hands-on Coding**: Follow along and write code as you learn
   - **Code-along**: Copy provided code if you get stuck
   - **Read-only**: Study the complete examples and run them directly


## Prepare your environment

1. **Setup UV**
   - Install uv: https://docs.astral.sh/uv/getting-started/installation/
      - If you are using PowerShell:
         - If you want to set your path, do this (replace your.username with actual name):
         ```pwsh
         $env:Path = "D:\Users\your.username\.local\bin;$env:Path".
         ```

         - If you want to set execution policy, use this command:
         
         ```pwsh
         Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
         ```

   - Set AWS credentials and AWS_REGION using env vars. Alternatively you can ser AWS profile.
   - Ensure that model us.anthropic.claude-3-7-sonnet-20250219-v1:0 is granted access from Bedrock service.
      - Or, if you want to use any other model just change the client.py code in each lesson.

