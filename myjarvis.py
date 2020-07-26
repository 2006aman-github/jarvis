import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

master="James"

def say(command):
    engine.say(command)
    engine.runAndWait()

def wish():
    global master
    hour = int(datetime.datetime.now().hour)
    if hour > 3 and hour < 11:
        say(f"Good Morning {master}")
    elif hour > 11 and hour < 16:
        say(f"Good Afternoon {master}")
    elif hour > 16 and hour < 24:
        say(f"Good Evening {master}")
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
        time.sleep(1)
        return query
    except:
        return "None"

        

if __name__ == "__main__":
    wish()
    say("How are You doing")
    say("I'am Jarvis and How can I help you..")
    while True:
        query = takeCommand().lower()  

        #Jarvis Logic
        if 'wikipedia' in query:
            say("Searching..Just a moment!")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            say(f"As Per my search. {result}")
        elif "hello" in query or "hi" in query:
            say(f"Hello {master}")
        elif query == None:
            say("I'm sorry I was not able to recognize that. Please Repeat")
        elif "how are you" in query or "how are you doing" in query:
            say(f"I'm fine {master}")


