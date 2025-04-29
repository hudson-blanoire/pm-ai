import sys
from dotenv import load_dotenv
import os

# Add the parent directory (workspace root) to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Load Environment Variables
load_dotenv()

# Import Libraries
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agents.google_agent import agent as google_agent
from agents.meeting_agent import agent as meeting_agent
from agents.research_agent import agent as research_agent
from agno.storage.sqlite import SqliteStorage

# Create Program Team
program_team = Team(
    name="Program Team",
    description="A team of agents that function in the role as a program manager automating tasks related to scheduling, emails, meetings, and research.",
    members=[google_agent, meeting_agent, research_agent],
    model=OpenAIChat(id="o3-mini"),
    markdown=True,
    show_tool_calls=True,
    mode="collaborate",
    enable_agentic_context=True,
    share_member_interactions=True,
    enable_team_history=True,
    num_of_interactions_from_history=5,
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
)

program_team.print_response("Please find the latest email I received from 'MIT Technology Review via LinkedIn'. Summarize the key discussion points and news assigned to me. Then, research the alternative technologies not mention in the email focusing on big news updates highlighting the latest developments. Based on this information and my current availability tomorrow afternoon (1 PM - 5 PM), schedule a 45-minute meeting named 'Commercialization Product Discovery Call' with 'hudsona03@vt.edu' via a Zoom Meeting and send a Google calendar invite to 'hudsona03@vt.edu' as well, including the email summary and a brief of the research you conducted in the meeting description. Finally, prepare a brief set of talking points for me for this meeting based on the email and research.", stream=True)
