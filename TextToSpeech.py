from openai import OpenAI
from playsound3 import playsound

def Speak(text: str, client: OpenAI) -> None:

	# create a file path to save the audio file
	file_path: str = 'speech.mp3'

	# create a new audio file
	response = client.audio.speech.create(
		model="tts-1",
		voice="onyx",
		input=text
	)

	# save the audio file
	response.stream_to_file(file_path)

	# play the audio file
	playsound(file_path)