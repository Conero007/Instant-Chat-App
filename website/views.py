from . import socketio
from flask_socketio import send
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@socketio.on('connect')
def connected():
    message = f'{current_user.name} has joined!'
    send(message, broadcast=True)


@socketio.on('disconnect')
def disconnected():
    message = f'{current_user.name} has left!'
    send(message, broadcast=True)


@socketio.on('message')
def send_message(text):
    message = f'{current_user.name}: {text}'
    send(message, broadcast=True)
