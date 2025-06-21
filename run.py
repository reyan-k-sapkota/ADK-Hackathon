import os
import json
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

remote_app = agent_engines.get(os.getenv('GOOGLE_CLOUD_AGENT_ID'))

print('\nWelcome to the Structural Engineering Consultant app.\nYou can exit any time after your conversation session begins by entering \'exit\'.\nBegin by entering a username in the prompt below.\n')

user_id = input('Enter your username: ')
session = remote_app.create_session(user_id=user_id)

sub_agent_name_map = {
        'Steel_Structures_Agent_prompt': 'Steel Structure Agent',
        'building_by_laws_agent': 'Building ByLaws Agent',
        'concrete_mix_design_agent_prompt': 'Concrete Mix Design Agent',
        'RCC_Structures_Agent_prompt': 'RCC Structure Agent'
    }

while True:
    query = input(f'[{user_id}]: ')
    if query.lower() == 'exit':
        break

    for event in remote_app.stream_query(
            user_id=user_id,
            session_id=session['id'],
            message=query,
        ):
        event_parts = event['content']['parts']

        for fragment in event_parts:
            if 'text' in fragment:
                print(fragment['text'])

            if 'function_call' in fragment:
                print(f'Consulting {sub_agent_name_map[fragment["function_call"]["name"]]}...')
