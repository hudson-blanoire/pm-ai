# Import Libraries
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

# Initialize Arxiv
arxiv = ArxivTools()

# Initialize Agent  
agent = Agent(
    name="Research Agent",
    model=OpenAIChat(id="o3-mini"),
    tools=[DuckDuckGoTools(), arxiv],
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    show_tool_calls=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
    add_datetime_to_instructions=True,
)
