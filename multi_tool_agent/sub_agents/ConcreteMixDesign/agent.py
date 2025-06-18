from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

academic_newresearch_agent = Agent(
    model=MODEL,
    name="concrete_miz_design_agent_prompt",
    instruction=prompt.CONCRETE_MIX_DESIGN_AGENT_PROMPT,
)