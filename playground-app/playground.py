import sys
import os

# Add the parent directory (workspace root) to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import Libraries
from agno.playground import Playground, serve_playground_app
# from agents.calendar_agent import agent as calendar_agent # Old
# from agents.email_agent import agent as email_agent       # Old
from agents.google_agent import agent as google_agent     # New
from agents.meeting_agent import agent as meeting_agent
from agents.research_agent import agent as research_agent
from team.program_team import program_team

# Load Agents
app = Playground(agents=[google_agent, meeting_agent, research_agent], teams=[program_team]).get_app()

# Launch App
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
