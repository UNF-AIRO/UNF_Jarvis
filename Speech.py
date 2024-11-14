import pyttsx3

#defining speak method allowing the program to make audio
def speak(message):
    #setting up the audio player
    engine = pyttsx3.init()

    #set speed of speach
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)

    #set volume of speech
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)

    #set voice of speech
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    #play audio
    engine.say(message)
    engine.runAndWait()
    engine.stop()