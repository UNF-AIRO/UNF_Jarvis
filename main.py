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

# Create a thread
jARVIS.Create_Thread('MAIN_THREAD')

"""
TTS Set Up
"""
import detection as dc
import Speech as s

# main loop
while True:
    # Listen for audio and convert to text
    userInput = dc.getSpeech()

    # send text to the assistant
    jARVIS.Create_Message(
        threadName='MAIN_THREAD',
        textContent=userInput
    )

    # get response from the assistant

    # response -> audio
    s.speak(userInput)
