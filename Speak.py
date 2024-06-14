import pyttsx3 
import datetime
import time

def Say(audio):
    engine = pyttsx3.init("sapi5") #sapi5 is microsaft speaking api/ software / engine- is our neck
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)  
    print("   ")
    print(f"Jarvis A.I : {audio}")
    engine.say(audio)
    print("   ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        Say(f"Good Morning Sir, its {tt}")

    elif hour >= 12 and hour <= 18:
        Say(f"Good Afternoon Sir, its {tt}")

    else:
        Say(f"Good Evening Sir, its {tt}")

    Say("Hii sir I am Jarvis, please tell me how may I help you?")




wishMe()            


