# Learning MCP

Learn Model Context Protocol (MCP) through hands-on examples.

## Quick Start

1. **Setup**
   - Install uv: https://docs.astral.sh/uv/getting-started/installation/
      - If you are using PowerShell:
         - If you want to set your path, do this (replace your.username with actual name):
```powershell
$env:Path = "D:\Users\your.username\.local\bin;$env:Path".
```  

         - If you want to set execution policy, use this command:
         
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
   - Set AWS credentials and AWS_REGION in env vars
   - Ensure that model us.anthropic.claude-3-7-sonnet-20250219-v1:0 is granted access from Bedrock service.
      - Or, if you want to use any other model just change the client.py code in each lesson.

2. **Run Lessons**
   - Navigate to any lesson folder (lesson-1, lesson-2, lesson-3)
   - Start with EXERCISE.md and follow the step-by-step instructions
   - If you get stuck, look at the provided code files (they contain the final answers)
   - Refer to README.md in each lesson for detailed concepts

## Lessons

- **lesson-1**: Basic MCP server with simple tools
- **lesson-2**: Weather data integration with external APIs  
- **lesson-3**: SQL database interaction with AI agents

Start with lesson-1 and work through each exercise file.
