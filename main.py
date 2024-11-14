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

print("Working...")

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
    responses: list[str] = jARVIS.Static_Response(
        threadName='MAIN_THREAD'
    )
    response = responses[0]

    # respone -> audio and play audio
    s.speak(text)
#<<<<<<< HEAD
    
#=======
    # play audio
#>>>>>>> c158f61f3263253e9165c6fb09d645c2c129fd56
