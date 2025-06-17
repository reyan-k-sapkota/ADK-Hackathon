from google.adk.agents import Agent

def get_pdf_url_for_country(country: str) -> str:
    urls = {
        "nepal": "https://giwmscdnone.gov.np/media/pdf_upload/NBC_205_READY-TO-USE_DETAILING_GUIDELINE_FOR-signed.pdf",
        "india": "https://civiconcepts.com/wp-content/uploads/2020/11/4.IS-10262-2019-New-Mix-design.pdf",
    }
    return urls.get(country.lower(), "")

# Define the agent
root_agent = Agent(
    name="engineering_code_consultant",
    model="gemini-2.0-flash",
    description="Provides region-specific consultation based on national engineering codes.",
    instruction=(
        "You are an engineering consultant AI that answers structural or civil engineering questions "
        "using national codes of practice. Use the `get_pdf_url_for_country` tool to retrieve the link of the relevant codes"
        "from the code document and cite page numbers when giving your answer."
    ),
    tools=[get_pdf_url_for_country],
)



