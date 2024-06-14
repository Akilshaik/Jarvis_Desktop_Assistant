from msilib.schema import File
from os import device_encoding
from pickletools import optimize
from random import shuffle
from xml.dom.minidom import CharacterData
import numpy as np
import json 
import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader
from NeutralNetwork import bag_of_words , tokenize , stem
from Brain import NeuralNet

with open('intents.json','r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w,tag))
        print(pattern)