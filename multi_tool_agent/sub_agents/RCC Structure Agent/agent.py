from google.adk import Agent
from . import prompt
import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
current_agent_dir = current_file_path.parent
sub_agents_dir = current_agent_dir.parent
sys.path.insert(0, str(sub_agents_dir))
from shared_tools import rag_response

MODEL = "gemini-2.0-flash"

root_agent = Agent(
        model=MODEL,
        name="RCC_Structures_Agent_prompt",
        instruction=prompt.RCC_STRUCTURE_AGENT_PROMPT,
        tools=[rag_response]
        )
