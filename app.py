from flask import Flask, render_template, make_response, redirect, request
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def registerClient():
    print('Client connected: ' + request.sid)
    clients.append(request.sid)

@socketio.on('disconnect')
def deleteClienet():
    print('Client disconnected: ' + request.sid)
    clients.remove(request.sid)

@socketio.on("mood")
def handleMessage(data):
    message = {
        "clients":clients,
        "from":request.sid,
        "content":data
    }
    emit("new_mood",json.dumps(message),broadcast=True)

@socketio.on("handPosition")
def handleMessage(data):
    message = {
        "clients":clients,
        "from":request.sid,
        "content":data
    }
    emit("new_handPosition",json.dumps(message),broadcast=True, skip_sid=request.sid)

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5004)
