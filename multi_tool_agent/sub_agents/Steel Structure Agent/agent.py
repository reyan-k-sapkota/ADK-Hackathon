from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

academic_newresearch_agent = Agent(
    model=MODEL,
    name="Steel_Structures_Agent_prompt",
    instruction=prompt.STEEL_STRUCTURE_AGENT_PROMPT,
)