""" author:partoo
    date:aug 2 2021
    purpose:speed up and offline text to speech
    """
import pyttsx3


def tts(string):
        engine = pyttsx3.init("espeak")
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[11].id)
        engine.say(string)
        engine.runAndWait()

if __name__ == '__main__':
    tts("hi, this sentence is for testing only.")
