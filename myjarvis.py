import threading
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import master_verify
import cv2
import os
import queue
import sys
sys.path.insert(1, 'C://my python programmin/ai_projects/Hand-Tracking Projects')
import VolumeControl
from neuralintents import GenericAssistant


# for automating the windows layout  on the screen these imports are made
# from pywinauto.findwindows    import find_window
# from pywinauto.win32functions import set



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 180)

def wish():
    global master

    hour = int(datetime.datetime.now().hour)
  
    if hour > 3 and hour <= 11:
        say(f"Good Morning sir, Jarvis at your service")
    elif hour > 11 and hour < 16:
       say(f"Good Afternoon sir, Jarvis at your service")
    elif hour > 16 and hour < 24:
        say(f"Good Evening sir, Jarvis at your service")
    else:
        say("hello")

VolCtrlTh = threading.Thread(target=VolumeControl.main)


def open_vol_control():
    global VolumeControlPr
    VolumeControlPr = {'status': True}
    say(f'Opening Volume Control')
    if master_detected["status"] == True:
              
            if VolumeControlPr["status"] == True:
                if VolCtrlTh.is_alive() == False:
                    VolCtrlTh = threading.Thread(target=VolumeControl.main)
                    VolCtrlTh.start()
                    
            if VolumeControlPr["status"] == False:
                VolumeControlPr = {'status': False}
                VolumeControl.stop()
            
def close_vol_control():
    pass

def shutdown_system():
    os.system("shutdown -s -t 0")

def open_browser():
    say("Opening the default Browser sir")
    webbrowser.open(url='http://github.com')
    # SetForegroundWindow(find_window(title='GitHub'))

def sleep_system():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
def respondToUser():
    say("Yes sir, I am here")
    

mappings = {"greeting": wish, "open_volumen_control": open_vol_control, "close_volume_control": close_vol_control, "shut_down_system": shutdown_system, "open_browser": open_browser, "sleep_system": sleep_system, "give_presence_res": respondToUser}
assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()
assistant.save_model()

master="Aman"





# protocol status vars 
VolumeControlPr = {'status': False}


def say(command):
    engine.say(command)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source, timeout=None)
    

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()
        print(f"You said: {query}")
        
        
        return query
    except:
        print("Didn't get that. Please repeat")
    
        
        return None
detectEffort = True
master_detected = {"status": False,  "means": "None"}


def runJarvis():
    global VolumeControlPr
    global detectEffort
    global master_detected
    print('Jarvis is running')
    if master_detected["status"] == False and detectEffort == True:
        detectResult = master_verify.main()
        master_detected = {"status": detectResult, "means": "Video"}
        if detectResult:
            print("[master detection]:", master_detected)
            detectEffort = False
            say('Welcome sir, Jarvis At your service.')
        else:
            detectEffort = False 
            say("Sorry, You dont have access to Jarvis")    
            return None
    
    while True:
        query = takeCommand()
            # verify master 
        if master_detected["status"] == False:
            detectResult = master_verify.main()
            master_detected = {"status": detectResult, "means": "Video"}   # if master detected
            if detectResult:
                print("[master detection]:", master_detected)
                detectEffort = False
                say('Welcome sir, Jarvis At your service.') 
        #Jarvis Logic
        try:
            assistant.request(query.lower())
        except:
            print(query)
            continue
        # if 'wikipedia' in query:
        #     say("Searching Wikipedia")
        #     query = query.replace("wikipedia", "")
        #     try:
        #         result = wikipedia.summary(query, sentences=2)
        #         say(f"As Per my search. {result}")
                
        #     except print(0):
        #         pass
        # elif "hello" in query or "hi" in query:
        #     say(f"Hello sir. I am Jarvis, How may I help you?")
        # elif query == None:
        #     say("I'm sorry I was not able to recognize that. Please Repeat")
        # elif "how are you" in query or "how are you doing" in query:
        #     say(f"I'm fine {master}")
        # elif "open volume control" in query:
        #     say(f'Opening Volume Control')
        #     VolumeControlPr = {'status': True}
        #     break
        # elif "close volume control" in query:
        #     say(f'Closing Volume Control')
        #     VolumeControlPr = {'status': False}
        #     break
        # elif ["shut", "system"] in query:
        #     say(f'Shutting down')
        #     break
    return None


if __name__ == "__main__":
    # wish()
    # say("I'am Jarvis and How can I help you..")

    # que = queue.Queue()
    # protocol status threads

   
    while True:
        # print(VolCtrlTh.is_alive())
        jarvisRes = runJarvis()
        if master_detected["status"] == True:
              
            if VolumeControlPr["status"] == True:
                if VolCtrlTh.is_alive() == False:
                    VolCtrlTh = threading.Thread(target=VolumeControl.main)
                    VolCtrlTh.start()
                    
            if VolumeControlPr["status"] == False:
                VolumeControlPr = {'status': False}
                VolumeControl.stop()
        

        # say("How are You doing"+master)
    



