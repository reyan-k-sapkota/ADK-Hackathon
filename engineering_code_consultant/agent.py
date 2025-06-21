from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.BuildingByLaws_Agent.agent import root_agent as building_bylaws_sub_agent
from .sub_agents.ConcreteMixDesign.agent import root_agent as concrete_mix_design_sub_agent
from .sub_agents.RCC_Structure_Agent.agent import root_agent as rcc_structure_sub_agent
from .sub_agents.Steel_Structure_Agent.agent import root_agent as steel_structure_sub_agent

root_agent = Agent(
    name="engineering_code_consultant",
    model="gemini-2.5-flash",
    description="Provides region-specific consultation based on national civil engineering codes.",
    instruction=prompt.CODE_COMPLIANCE_CONSULTANT_AGENT_PROMPT,
    tools=[AgentTool(agent=building_bylaws_sub_agent),
           AgentTool(agent=concrete_mix_design_sub_agent),
           AgentTool(agent=rcc_structure_sub_agent),
           AgentTool(agent=steel_structure_sub_agent)
        ]
)
