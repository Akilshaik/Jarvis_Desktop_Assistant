#Function
from calendar import day_abbr
import datetime
import email
from email import message
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fileinput import filename
from http import server
import json
from json import encoder
from logging.config import listen
from platform import python_branch
from random import random
import smtplib
from tracemalloc import start
from unittest import result
from winsound import PlaySound
import PyPDF2
from numpy import polymul
import pyjokes
import gtts
from pywikihow import search_wikihow


from bs4 import BeautifulSoup, Tag
from googletrans import Translator
from gtts import gTTS
from h11 import Data
import pywhatkit
from requests import get, request
import requests
from Listen import Listen
from Speak import Say 
import datetime
import os
import webbrowser
import cv2
import sys
import pyautogui
import time
import random
import keyboard
import newsapi
from newsapi import NewsApiClient

#Non Input

def Time():
        time = datetime.datetime.now().strftime("%H:%M%p")
        Say(time)

def Date():
        date = datetime.date.today()
        Say(date)

def Day():
        day = datetime.datetime.now().strftime("%A")
        Say(day)
      
def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()  

    elif "day" in query:
        Day() 

    elif 'open notepad' in query:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath) 

    elif 'close notepad'in query:
            os.system("TASKKILL /F /im notepad.exe")     

    elif 'open excel' in query:
        excelpath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe"
        os.startfile(excelpath)    

    elif 'close excel'in query:
            os.system("TASKKILL /F /im EXCEL.exe")

    elif 'open word' in query:
        wordpath = "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\WINWORD.exe"
        os.startfile(wordpath)

    elif 'close word'in query:
            os.system("TASKKILL /F /im WINWORD.exe")    

    elif 'close chrome' in query:
        chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromepath)

    elif 'close chrome'in query:
            os.system("TASKKILL /F /im chrome.exe")    

    elif 'open vlc' in query:
        vlcpath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
        os.startfile(vlcpath)      

    elif 'close vlc'in query:
            os.system("TASKKILL /F /im vlc.exe")

    elif 'open cmd' in query:
        cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
        os.startfile(cmdpath)    

    elif 'open webbrowser' in query:
        msdpath = "C:\\WINDOWS\\system32\\msedge.exe"
        os.startfile(msdpath)    

    elif 'close cmd'in query:
            os.system("TASKKILL /F /im cmd.exe") 

    elif 'close webbrowser'in query:
            os.system("TASKKILL /F /im msedge.exe")   

    elif 'joke' in query:
            get = pyjokes.get_joke()
            Say(get)                        

    elif 'ip address' in query:
        ip = get('https://api.ipify.org').text      
        Say(f"your IP address is {ip}")   

    elif 'alarm' in query:
            Say("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Say("Time To Wake Up Sir!")
                    PlaySound('iron.mp3')
                    Say("Alarm Closed!")

                elif now>time:
                    break             

    elif "go baby go" in query:
        os.system("shutdown /s /t 5")

    elif "run baby run" in query:
        os.system("shutdown /r /t 5")

    elif "all is well" in query:
        os.system("rund1132.exe powrprof.dil,SetSuspendState 0,1,0")  

    elif 'switch the window' in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt") 

    elif "play music" in query:
        music_dir = "D:\\music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))   

    elif 'repeat my word' in query:
            Say("Speak Sir!")
            jj = Listen()
            Say(f"You Said : {jj}")          
        

    elif 'my location' in query:
            Say("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

    elif "close map" in query:
        os.system("taskkill /im msedge.exe /f")                  
                        
    elif 'pause' in query:
            keyboard.press('space bar')

    elif 'restart' in query:
            keyboard.press('0')

    elif 'mute' in query:
            keyboard.press('m')

    elif 'skip' in query:
            keyboard.press('l')

    elif 'back' in query:
            keyboard.press('j')

    elif 'full screen' in query:
            keyboard.press('f')

    elif 'film mode' in query:
            keyboard.press('t')

    elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

    elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

    elif 'history' in query:
            keyboard.press_and_release('ctrl +h')                     

    elif 'camera' in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(20)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWindows() 

    elif "screenshot" in query:
        screenshot()    

    elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Say("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

    elif 'what do you remember' in query:
        remeber = open('data.txt','r')
        Say("You Tell Me That" + remeber.read())    

    elif 'you need a break' in query:
            Say("Ok Sir , You Can Call Me Anytime !")
            Say("Just Say Wake Up Jarvis!")
            sys.exit()    
   
            
    Say("sir, do you have any other work")     


#Input

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(query, sentences=2)
        Say("according to wikipedia")
        Say(result)

    elif "open google" in tag:
        Say("sir what should I search for?")
        query = Listen().lower()
        topic = str(query).replace("open google","")
        topic = query.replace("search","").replace("open google","")
        Say('Searching ' + topic)
        pywhatkit.search(topic)

    elif 'close google'in query:
            os.system("taskkill /im msedge.exe /f")    

    elif 'open youtube' in tag: 
        Say("What should I search on youtube")
        query = Listen()       
        topic = query.replace('open youtube', '')
        Say('playing ' + topic)    
        pywhatkit.playonyt(topic)

    elif 'how to' in query:
            Say("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Say(how_to_func[0].summary)    

    elif "close youtube" in query:
        os.system("taskkill /im msedge.exe /f")

    elif "open instagram" in tag:
        webbrowser.open("www.instagram.com")

    elif "close instagram" in query:
        os.system("taskkill /im msedge.exe /f")    
    
    elif "open facebook" in tag:
        webbrowser.open ("www.facebook.com")

    elif "close facebook" in query:
        os.system("taskkill /im msedge.exe /f")          
    
    elif "temperature" in tag:
        Temp()

    elif "news" in tag:
        news()    

    elif 'website' in tag:
            Say("Ok Sir , Launching.....")
            query = query.replace("open","").replace("jarvis","")
            query = query.replace(" ","")
            web1 = query.replace("website","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Say("Launched!")   

    elif 'launch' in tag:
            Say("Tell Me The Name Of The Website!")
            query = Listen()
            web = 'https://www.' + query + '.com'
            webbrowser.open(web)
            Say("Done Sir!")        

    elif "current location" in tag:
        Say("wait a sec sir, let me check")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)   
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            Say(f"sir I am not sure, but i think we are in {city} city of {country} country")
        except Exception as e:
            Say(f"sorry sir, due to network issue i am not able to find where we are.")
            pass

    elif 'pause' in tag:
            keyboard.press('space bar')

    elif 'restart' in tag:
            keyboard.press('0')

    elif 'mute' in tag:
            keyboard.press('m')

    elif 'skip' in tag:
            keyboard.press('l')

    elif 'back' in tag:
            keyboard.press('j')

    elif 'full screen' in tag:
            keyboard.press('f')

    elif 'film mode' in tag:
            keyboard.press('t')

    elif 'close the tab' in tag:
            keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in tag:
            keyboard.press_and_release('ctrl + t')

    elif 'open new window' in tag:
            keyboard.press_and_release('ctrl + n')

    elif 'history' in tag:
            keyboard.press_and_release('ctrl +h')     


def news():
    api_dict = {"bussiness" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "bussiness IN" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "entertainment IN" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "health IN" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "science" : "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "science IN" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "sports" : "https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "sports IN" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "technology" : "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=ce4eaf35847a443fa45dcb8ca930f920",
                "technology IN" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ce4eaf35847a443fa45dcb8ca930f920",

}
    content = None
    url = None
    Say("Which field news do you want, bussiness , health , entertainment , science , technology , sports ?")
    field = input("Type filed news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
            print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Say("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Say(article)
        news_url = articles["url"]
        print(f"for more information visit: {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    Say("that's it for now i'll update you in some time")
  


def Temp(tag,query):
        if "temperature" in tag:
            tag = "temperature"
            url = f"https://www.google.com/search?q={tag}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Say(f"The Temperature Outside Is {temperature} celcius")

            Say("Do I Have To Tell You Another Place Temperature ?")
            query = Listen()

        if 'yes' in query:
            Say("Tell Me The Name Of tHE Place ")
            query = Listen()
            tag = f"temperature in {query}"
            url = f"https://www.google.com/search?q={tag}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Say(f"The Temperature in {query} is {temperature} celcius")

        else:
            Say("no problem sir")    


def screenshot():
        Say("Ok Boss , What Should I Name That File ?")
        path = Listen()
        path1name = path + ".png"
        path1 = "C:\\Users\\salvi\\Pictures\\JarvisScreenST\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\salvi\\Pictures\\JarvisScreenST\\")
        Say("Here Is Your ScreenShot")                     

                        


   
        
        
#Say("sir, do you have any other work")




            



