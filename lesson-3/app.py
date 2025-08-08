from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_aws import ChatBedrock

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Question(BaseModel):
    question: str

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.post("/ask")
async def ask_question(question: Question):
    llm = ChatBedrock(model="us.anthropic.claude-3-7-sonnet-20250219-v1:0")
    client = MultiServerMCPClient({
        "sql_database": {
            "url": "http://localhost:50873/sse",
            "transport": "sse",
        }
    })
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    
    response = await agent.ainvoke({"messages": question.question})
    return {"answer": response['messages'][-1].content}