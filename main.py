"""
Assistant Set Up
"""
# Imports
from Assistant2 import Assistant_V2
from openai import OpenAI
from dotenv import load_dotenv
from os import environ, system
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

system('cls')
print("Working...")

# main loop
while True:
    # Listen for audio and convert to text
    userInput = dc.getSpeech()
    print(f"User: {userInput}\n")

    # send text to the assistant
    jARVIS.Create_Message(
        threadName='MAIN_THREAD',
        textContent=userInput
    )

    # get response from the assistant
    responses: list[str] = jARVIS.Static_Response(
        threadName='MAIN_THREAD'
    )
    response = responses[0]
    print(f"Jarvis: {response}\n")

    # respone -> audio and play audio
    s.speak(response)
