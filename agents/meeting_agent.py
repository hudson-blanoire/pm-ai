# Import Libraries
from agno.agent import Agent
from agno.tools.zoom import ZoomTools
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

# Initialize Zoom tools with credentials
zoom_tools = ZoomTools(
    account_id=os.getenv("ZOOM_ACCOUNT_ID"),
    client_id=os.getenv("ZOOM_CLIENT_ID"),
    client_secret=os.getenv("ZOOM_CLIENT_SECRET")
)

# Create an agent with Zoom capabilities
agent = Agent(
    name="Meeting Agent",
    model=OpenAIChat(id="o3-mini"),
    tools=[zoom_tools], 
    show_tool_calls=True,
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)
