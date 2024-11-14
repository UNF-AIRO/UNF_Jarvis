"""
Assistant Set Up
"""
# Imports
from Assistant2 import Assistant_V2
from openai import OpenAI
from dotenv import load_dotenv
from os import environ
load_dotenv()

# Create an instance of the assistant
jARVIS: Assistant_V2 = Assistant_V2(
    client=OpenAI(
        api_key=environ['OPENAI_API_KEY']
    ),
    id=environ['ASSISTANT_ID']
)

# main loop
while True:
    # Listen for audio

    # audio -> text

    # send text to the assistant

    # get response from the assistant

    # response -> audio

    # play audio
    break

print("Done")