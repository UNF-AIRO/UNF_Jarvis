from pathlib import Path
from openai import OpenAI
from playsound import playsound
client = OpenAI(api_key= '')

def speak(text):
    text = text.replace('nova','')
    file_path = 'speech.mp3'
    response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=text
)

    response.stream_to_file(file_path)
    playsound("speech.mp3")
    playsound

