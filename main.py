import GetInput
import speech
import detection as dc

if __name__ == "__main__":
    speech.speak("Hello Sir if you need anything please just call my name")
    while True:
        start = dc.starting()
        if start:
            selections = dc.selection()

            if selections == "off":
                speech.speak("Glab to help powering off")
                break

        else:
            continue
