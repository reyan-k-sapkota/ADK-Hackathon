import os
import vertexai
from vertexai import agent_engines
from beaver_assist_agent.agent import root_agent
from vertexai.preview import reasoning_engines

PROJECT_ID = os.getenv(PROJECT_ID)
LOCATION = os.getenv(LOCATION)
STAGING_BUCKET = os.getenv(STAGING_BUCKET)

vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET,
    )

app = reasoning_engines.AdkApp(
        agent=root_agent,
        enable_tracing=True,
        )

remote_agent = agent_engines.create(
        app,
        requirements=[
            'google-cloud-aiplatform[agent_engines,adk]',
         ],
        display_name="Beaver Assist Agent",
        description="An ADK agent that specializes in structural engineering codes for India and Nepal",
        extra_packages=[
            "./beaver_assist_agent",
        ]
    )

print(f"Agent deployed: {remote_agent.resource_name}")
