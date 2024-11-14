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
    # Listen for audio and convert to text
    text = dc.getSpeech()
    # send text to the assistant

    # get response from the assistant

    # respone -> audio and play audio
    s.speak(text)
#<<<<<<< HEAD
    
#=======
    # play audio
#>>>>>>> c158f61f3263253e9165c6fb09d645c2c129fd56
