import random
import json
from bs4 import BeautifulSoup
import requests
import torch
from Brain import NeuralNet
from NeutralNetwork import bag_of_words ,tokenize
import webbrowser
import datetime
import os
import cv2 
import newsapi
import nltk



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size= data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#--------------------------------------------
Name = "Jarvis"

from Listen import Listen
from Speak import Say
from task import NonInputExecution,news
from task import InputExecution
from task import Temp
from task import news 

def Main():

    sentence = Listen()

    result = str(sentence)

    if sentence == "exit":
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["responses"])
                
                if "time" in reply:
                    NonInputExecution(reply)    

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply) 

                elif "joke" in reply:
                    NonInputExecution(reply)    

                elif "wikipedia" in reply:
                    Say("searching wikipedia")
                    InputExecution(reply,result)  

                elif "open google" in reply:
                    InputExecution(reply,result)  

                elif 'close google' in reply:
                    Say("ok sir, closing google")
                    InputExecution(reply,result)

                elif 'open youtube' in reply:
                    InputExecution(reply,result)  

                elif 'open notepad' in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply)       

                elif 'open excel' in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply) 

                elif 'close excel' in reply:
                    Say("ok sir, closing excel")
                    NonInputExecution(reply)      

                elif 'open word' in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply)

                elif 'close word' in reply:
                    Say("ok sir, closing word")
                    NonInputExecution(reply)     

                elif 'open chrome' in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply) 

                elif 'close chrome' in reply:
                    Say("ok sir, closing chrome")
                    NonInputExecution(reply)      

                elif 'open vlc' in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply) 

                elif 'close vlc' in reply:
                    Say("ok sir, closing vlc")
                    NonInputExecution(reply)    

                elif "open cmd" in reply:
                    Say("Ok Sir , Wait A Second!")
                    NonInputExecution(reply)

                elif 'close cmd' in reply:
                    Say("ok sir, closing cmd")
                    NonInputExecution(reply)    

                elif "camera" in reply:
                    Say("Ok Sir , Wait A Second!")
                    Say("Your Command Has Been Completed Sir!")
                    NonInputExecution(reply)  

                elif "ip address" in reply:
                    NonInputExecution(reply)    

                elif "open youtube" in reply:
                    Say("Sure sir")
                    Say("Youtube is open sir")
                    InputExecution(reply,result) 

                elif "close youtube" in reply:
                    Say("Okay sir, Closing youtube")      
                    InputExecution(reply,result)
                    
                elif "open instagram" in reply:
                    Say("Sure sir")
                    Say("instagram website is open sir")
                    InputExecution(reply,result)   

                elif "close instagram" in reply:
                    Say("Okay sir, Closing instagram")      
                    InputExecution(reply,result)      

                elif "open facebook" in reply:
                    Say("Sure sir")
                    Say("facebook website is open sir")
                    InputExecution(reply,result) 

                elif "close facebook" in reply:
                    Say("Okay sir, Closing facebook")      
                    InputExecution(reply,result)               
                    
                elif "you need a break" in reply:
                    NonInputExecution(reply)

                elif 'close notepad' in reply:
                    Say("Okay sir, closing notepad")
                    NonInputExecution(reply)  

                elif 'alarm' in reply:
                    Say("Okay sir")      
                    NonInputExecution(reply)

                elif 'switch the window' in reply:
                    Say("Switching windows")
                    NonInputExecution(reply)    

                elif "go baby go" in reply:
                    Say("Sure, shutting down your lappy")
                    NonInputExecution(reply)

                elif "run baby run" in reply:
                    Say("Sure, restarting down your lappy")
                    NonInputExecution(reply)

                elif "all is well" in reply:
                    Say("Sure, sleeping down your lappy")
                    NonInputExecution(reply)  

                elif "news" in reply:
                    InputExecution(reply,result)  

                elif "current location" in reply:
                    InputExecution(reply,result)

                elif "play music" in reply:
                    Say("Playing music")
                    NonInputExecution(reply)  
                    Say("Enjoy the song sir") 

                elif "website" in reply:
                    InputExecution(reply,result)     

                elif "launch" in reply:
                    InputExecution(reply,result)    

                elif "temperature" in reply:
                    Temp(reply,result)    

                elif "repeat my word" in reply:
                    NonInputExecution(reply) 

                elif "remember that" in reply:
                    NonInputExecution(reply)    

                elif "what do you remember" in reply:
                    NonInputExecution(reply)   

                elif "how to" in reply:
                    InputExecution
                    (reply,result)     

                elif "my location" in reply:
                    NonInputExecution(reply)

                elif "close map" in reply:
                    NonInputExecution(reply)   

                elif "screenshot" in reply:
                    NonInputExecution(reply)      

                elif "pause" in reply:
                    NonInputExecution(reply)

                elif "restart" in reply:
                    NonInputExecution(reply)

                elif "mute" in reply:
                    NonInputExecution(reply)

                elif "skip" in reply:
                    NonInputExecution(reply)

                elif "back" in reply:
                    NonInputExecution(reply)

                elif "full screen" in reply:
                    NonInputExecution(reply) 

                elif "film mode" in reply:
                    NonInputExecution(reply) 

                elif "youtube tool" in reply:
                    NonInputExecution(reply)

                elif "close the tab" in reply:
                    NonInputExecution(reply)

                elif "open new tab" in reply:
                    NonInputExecution(reply)

                elif "open new window" in reply:
                    NonInputExecution(reply)

                elif "history" in reply:
                    NonInputExecution(reply)  
                                              


                else:
                    Say(reply)        


#while True:
 #   Main ()

          


