import speech_recognition as sr

def Get_Speech(micIndex: int) -> str:
    # create a speech recognizer
    r = sr.Recognizer()

    # loop until speech is detected
    while True:
        try:
            # connect to the microphone
            with sr.Microphone(micIndex) as mic:

                # remove abient noise from the audio
                r.adjust_for_ambient_noise(mic, duration=2)

                # listen for speech and convert sound to text
                text: str = r.recognize_google(r.listen(mic)).lower()

                # check if the user said "jarvis"
                if "jarvis" in text:
                    return text
                
        except sr.UnknownValueError:
            # if speech is not detected, try again
            r = sr.Recognizer()

def Select_Microphone() -> int:
    # get all available microphones
    microphones: list[str] = sr.Microphone.list_microphone_names()
    # print the available microphones
    for i, microphone in enumerate(microphones):
        print(f"{i}: {microphone}")

    # prompt the user to select a microphone
    selectedMicrophone: int = int(input("Select a microphone: "))

    # return the selected microphone
    return selectedMicrophone