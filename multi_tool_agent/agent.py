from google.adk.agents import Agent
from . import prompt


def get_pdfs(country: str) -> str:
    urls = {
        "british_Concrete_Mix_Design": "https://openscience.utm.my/server/api/core/bitstreams/055460e4-8c16-4dd1-af21-a1ae209b02bc/content",
        "india_Concrete_Mix_Design": "https://civiconcepts.com/wp-content/uploads/2020/11/4.IS-10262-2019-New-Mix-design.pdf",
        "american_Concrete_Mix_Desgin":"https://drive.google.com/drive/u/1/folders/1pbEjyebvwaO6SD2XU5_pZRN__kSt2z4T",
        
    }
    return urls.get(country.lower(), "")



# Define the agent
root_agent = Agent(
    name="engineering_code_consultant",
    model="gemini-2.0-flash",
    description="Provides region-specific consultation based on national civil engineering codes.",
    instruction=prompt.CODE_COMPLIANCE_CONSULTANT_AGENT,
    tools=[get_pdfs],
)



