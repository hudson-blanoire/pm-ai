import sys
import os

# Add the parent directory (workspace root) to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from agents.google_agent import agent as google_agent

print("Attempting to authenticate and fetch scopes for Google Calendar and Gmail...")

try:
    # Call a Calendar function first
    print("\nCalling Calendar Tool (list_events)...")
    google_agent.run("List my events for today", stream=False) # Use run instead of print_response for cleaner output
    print("Calendar tool call attempted.")
except Exception as e:
    print(f"Error during Calendar call (this might be expected if auth flow is needed): {e}")

try:
    # Immediately call a Gmail function
    print("\nCalling Gmail Tool (get_latest_emails)...")
    google_agent.run("Get my latest email", stream=False)
    print("Gmail tool call attempted.")
except Exception as e:
    print(f"Error during Gmail call (this might be expected if auth flow is needed): {e}")

print("\nAuthentication script finished. Please check the console for any Google authorization URLs.")
print("If prompted, visit the URL, grant permissions for BOTH Calendar and Gmail.")
print("Once authorized, a new agents/token.json should be created with combined scopes.")
print("You can now run your team/program_team.py script.") 