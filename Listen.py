from cv2 import phase
import speech_recognition as sr

from Speak import Say

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("           ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}\n")   

    except Exception as e:
        Say("Say that again please....")
        return "none"    

    query = str(query)
    return query.lower()   

Listen()             