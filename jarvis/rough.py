import time

import pyttsx3

engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')       #getting details of current voice
# print(voices[4].id)
print(len(voices))
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
for i in range(69):
    time.sleep(2)
    print(i)
    engine.setProperty('voice', voices[i].id)   #changing index, changes voices. 1 for female
    engine.setProperty('rate', 178)   #changing index, changes voices. 1 for female
    print(voices[i],id)
    engine.say("Hello World!")
    engine.say('My current speaking rate is ')
    engine.runAndWait()
    engine.stop()


