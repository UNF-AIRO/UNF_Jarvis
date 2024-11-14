import pyttsx3

def speak(message):
    engine = pyttsx3.init()


    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)

    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(message)
    engine.runAndWait()
    engine.stop()