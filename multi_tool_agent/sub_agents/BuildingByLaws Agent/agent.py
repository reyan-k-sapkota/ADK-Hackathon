from google.adk import Agent

from . import prompt



MODEL = "gemini-2.0-flash"

academic_newresearch_agent = Agent(
    model=MODEL,
    name="building_by_laws_agent",
    instruction=prompt.NEPAL_BYLAWS_AGENT_PROMPT,
)