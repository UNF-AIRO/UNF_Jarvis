import speech_recognition as sr

#method to detect speech from user
def getSpeech():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                #remove abient noise from the audio
                r.adjust_for_ambient_noise(mic, duration = 0.2)
                #get audio input
                audio = r.listen(mic)
                #convert audio to String
                text = r.recognize_google(audio)
                #convert text to lowercase
                text = text.lower()
                #returns audio with primer command
                if "jarvis" in text:
                    return
        #make sure the program keeps looping if bad audio is given
        except sr.UnknownValueError:
            r = sr.Recognizer()
            continue