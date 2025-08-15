import asyncio
import time

from mcp_agent.app import MCPApp
from mcp_agent.config import (
    BedrockSettings,
    Settings,
    LoggerSettings,
    MCPSettings,
    MCPServerSettings,
)
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_bedrock import BedrockAugmentedLLM


# Settings can either be specified programmatically,
# or loaded from mcp_agent.config.yaml/mcp_agent.secrets.yaml
app = MCPApp(
    name="mcp_basic_agent"
)


async def example_usage():
    async with app.run() as agent_app:
        logger = agent_app.logger
        context = agent_app.context

        logger.info("Current config:", data=context.config.model_dump())

        finder_agent = Agent(
            name="agent1",
            instruction="""You are an agent with the ability to fetch URLs. You can also query database.""",
            server_names=["fetch","sqlite"],
        )

        async with finder_agent:
            logger.info("agent1: Connected to server, calling list_tools...")
            result = await finder_agent.list_tools()
            logger.info("Tools available:", data=result.model_dump())

            llm = await finder_agent.attach_llm(BedrockAugmentedLLM)

            result = await llm.generate_str(
                message="Fetch https://example.com",
            )
            logger.info(f"Content from example.com: {result}")            

            result = await llm.generate_str(
                message="Find out total number of customers in the database.",
            )
            logger.info(f"Total customers result: {result}")

            result = await llm.generate_str(
                message="What was the question.",
            )
            logger.info(f"Recall original quetion results: {result}")

            result = await llm.generate_str(
                message="What SQl was used to answer previous question",
            )
            logger.info(f"Recall SQL statement: {result}")



if __name__ == "__main__":
    start = time.time()
    asyncio.run(example_usage())
    end = time.time()
    t = end - start

    print(f"Total run time: {t:.2f}s")