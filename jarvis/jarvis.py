#!/usr/bin/env python3
""" author:partoo
    date:aug 2 2021
    purpose:virtual AI
"""
# import pyttsx3
import random
import pyaudio
import mytts
import datetime
#import speech_recognition as sr
import wikipedia
import mytts_offline
import webbrowser
import os
from playsound import playsound
import smtplib
import pywhatkit
import pyjokes

global audiop
def speak(audio):
    # speak function
    if audiop == 1:
        mytts.tts(audio)
    else:
        mytts_offline.tts(audio)
    print(audio)
    return

def wishme():
    # wish at start
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    return

def takecommand():
    # takes mic input from the user and returns string

    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("listening...")
    #     # r.energy_threshold = 350
    #     audio = r.listen(source)
    #
    # try:
    #     print("Recognising...")
    #     query = r.recognize_google(audio,language="en-US")
    #     print("User said: "+ query+"\n")
    #
    # except Exception as e:
    #     print(e)
    #     print("Say that again please...")
    #     return "None"
    # return query

    string = input("listening..\n")
    return string

def sendEmail(to,content):
    #function to send email
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    with open("/home/pro123/Downloads/ad.txt") as f:
        p=f.read()
    server.login("codingcreation3.9.8@gmail.com",p)
    server.sendmail("codingcreation3.9.8@gmail.com",to,content)
    server.close()


if __name__ == '__main__':
    audiop = int(input("Enter 1 for online speech."))
    wishme()
    while True:
        query = takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query = query.replace("wikipedia","")
            results  = wikipedia.summary(query,sentences=2)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = r"/home/partoo/Music/English/"
            music = os.listdir(music_dir)
            song = music[random.randint(0,len(music))]
            print(song)
            playsound(music_dir+song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"The time is {strTime}")

        elif "open app" in query:
            query_list = query.split(" ")
            app_index = query_list.index("app") + 1
            os.system(query_list.__getitem__(app_index))
            # print(query_list.__getitem__(app_index))

        elif 'email' in query:
            speak("Enter email address: ")
            to =  input()
            speak("what should I say: ")
            try:
                content = takecommand()
                # to = 'partoodeka2825@gmail.com'
                sendEmail(to,content)
                speak("Your email has been sent.")
            except Exception as e:
                speak("sorry sir,There was a problem.\nproblem:"+e)
	

        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'github' in query:
            webbrowser.open("github.com")
        
        elif 'sports news' in query:
            os.system("python3 /home/pro123/PycharmProjects/codewithharry/sports.py")
        
        elif 'news' in query:
            os.system("python3 /home/pro123/PycharmProjects/codewithharry/ex9.py")
        elif 'play on yt' in query:
            query2 = query.replace('play on yt','')
            pywhatkit.playonyt(query2)
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'quit' in query:
            exit()
