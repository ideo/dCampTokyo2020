'''
This is a Python script to log
incoming Socket IO messages to
a text file.
'''

# -*- coding: utf-8 -*-
import socketio
import time
from datetime import datetime
import json

# prepare log file
currentTime = datetime.now().strftime('%Y%m%d%H%M%S')
logFile = open("txt/" + currentTime + ".txt","w")

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def new_mood(msg):
    print('[{}] response : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S') , msg))
    messageJSON = json.loads(msg)
    currentEpochTime = int(time.time())
    logFile.write(str(currentEpochTime) + " " + str(messageJSON["from"]) + " " + str(messageJSON["content"]) + "\n") #write to logFile

@sio.event
def disconnect():
    print('disconnected from server, closing log file')
    logFile.close()

sio.connect('https://dcamptokyo2020.herokuapp.com')
sio.wait()
