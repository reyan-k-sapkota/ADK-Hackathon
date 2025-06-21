import os
import vertexai
from vertexai import agent_engines
from engineering_code_consultant.agent import root_agent
from vertexai.preview import reasoning_engines
from dotenv import load_dotenv

load_dotenv()

vertexai.init(
        project=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION"),
        staging_bucket=os.getenv("GOOGLE_CLOUD_STAGING_BUCKET"),
    )

app = reasoning_engines.AdkApp(
        agent=root_agent,
        enable_tracing=True,
        )

remote_agent = agent_engines.create(
        agent_engine=app,
        requirements=[
            'google-cloud-aiplatform[agent_engines,adk]',
         ],
        display_name="Beaver Assist Agent",
        description="An ADK agent that specializes in structural engineering codes for India and Nepal",
        extra_packages=[
            "./engineering_code_consultant",
        ]
    )

print(f"Agent deployed: {remote_agent.resource_name}")
