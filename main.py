from Assistant2 import Assistant, Language_Model
#from dotenv import load_dotenv
import detection as dc
import Speech as s

# main loop
while True:
    # Listen for audio and convert to text
    text = dc.getSpeech()
    # send text to the assistant

    # get response from the assistant

    # response -> audio
    s.speak(text)
    # play audio