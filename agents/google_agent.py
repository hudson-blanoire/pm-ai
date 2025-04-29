# Import Libraries
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlecalendar import GoogleCalendarTools
from agno.tools.gmail import GmailTools
from agno.storage.sqlite import SqliteStorage
import datetime
from tzlocal import get_localzone_name
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

# --- Configuration --- 
# Load paths from environment variables. Provide defaults or raise errors if not set.
# IMPORTANT: Ensure GOOGLE_CREDENTIALS_PATH is set in your .env file or system environment.
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")
if not CREDENTIALS_PATH:
    raise ValueError("Environment variable GOOGLE_CREDENTIALS_PATH is not set. Please provide the path to your Google OAuth credentials JSON file.")

# Token path can default if not specified
TOKEN_PATH = os.getenv("GOOGLE_TOKEN_PATH", "agents/token.json") 
# Ensure the directory for the token exists
os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)

# Database path can default
DB_PATH = os.getenv("DATABASE_PATH", "tmp/data.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
# --- End Configuration ---

agent = Agent(
    name="Google Assistant Agent",
    model=OpenAIChat(id="o3-mini"),
    tools=[
        GoogleCalendarTools(
            credentials_path=CREDENTIALS_PATH, 
            token_path=TOKEN_PATH
        ),
        GmailTools(
            credentials_path=CREDENTIALS_PATH, 
            token_path=TOKEN_PATH
        )
    ],
    show_tool_calls=True,
    instructions=[
        f"""
        You are a helpful assistant for managing Google Calendar and Gmail. Today is {datetime.datetime.now()} and the user's timezone is {get_localzone_name()}.
        You should help users to perform these actions:
            - Get scheduled events from Google Calendar.
            - Create events in Google Calendar.
            - Read emails from Gmail.
            - Send emails using Gmail.
            - Draft emails in Gmail.
        """
    ],
    storage=SqliteStorage(table_name="agent_sessions", db_file=DB_PATH),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)
