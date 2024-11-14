import speech_recognition as sr

#method to detect speech from user
def getSpeech():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration = 0.2)
        except:
