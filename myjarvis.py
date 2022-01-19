import threading
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import master_verify
import cv2
import os
import sys
sys.path.insert(1, 'C://my python programmin/ai_projects/Hand-Tracking Projects')
import VolumeControl



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 170)

master="Aman"


def say(command):
    engine.say(command)
    engine.runAndWait()

def wish():
    global master
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour > 3 and hour < 11:
        say(f"Good Morning ")
    elif hour > 11 and hour < 16:
        say(f"Good Afternoon ")
    elif hour > 16 and hour < 24:
        say(f"Good Evening ")
    else:
        say("hello")

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = None)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        
        return query
    except:
        return "None"


def runJarvis():
    detectEffort = True
    master_detected = {"status": False,  "means": "None"}
    print('Jarvis is running')
    if master_detected["status"] == False and detectEffort == True:
        detectResult = master_verify.main()
        master_detected = {"status": detectResult, "means": "Video"}
        if detectResult:
            print(master_detected)
            say('Welcome sir, Jarvis At your service.')
        else:
            detectEffort = False 
            say("Sorry, You dont have access to Jarvis")    
            return None
    while True:
        query = takeCommand().lower()
            # verify master 

        #Jarvis Logic
        if 'wikipedia' in query:
            say("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                say(f"As Per my search. {result}")
                
            except print(0):
                pass
        elif "hello" in query or "hi" in query:
            say(f"Hello sir. I am Jarvis. How may I help you?")
        elif query == None:
            say("I'm sorry I was not able to recognize that. Please Repeat")
        elif "how are you" in query or "how are you doing" in query:
            say(f"I'm fine {master}")
        elif "open volume control" in query:
            say(f'Opening Volume Control')
            volControlTh = threading.Thread(VolumeControl.main(), ())
            volControlTh.start()
        elif "close volume control" in query:
            say(f'Closing Volume Control')
            

if __name__ == "__main__":
    # wish()
    # say("I'am Jarvis and How can I help you..")
    runJarvis()
    # say("How are You doing"+master)
    



