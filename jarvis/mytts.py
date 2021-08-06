from gtts import gTTS
import playsound
import pyttsx3


def tts(string):
    try:
        speak = gTTS(text=string,lang ='hi')
        speak.save("mytts.mp3")
        playsound.playsound("mytts.mp3")

    except Exception as e:
        print("Error using google tts service, running in 'pyttsx3'")
        engine = pyttsx3.init("espeak")
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[11].id)
        engine.say(string)
        engine.runAndWait()

if __name__ == '__main__':
    tts("hi, this sentence is for testing only.")
