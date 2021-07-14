import time
from . import socketio, db
from .models import Chat, User
from flask_socketio import send, emit
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect

views = Blueprint("views", __name__)


@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user, messages=Chat, all_user=User)


@socketio.on('exit_chat')
def exit_chat():
    current_user.online = False
    db.session.commit()

    time.sleep(60000)
    if current_user.online == False:
        emit('refresh_page')
        print(f'\n\n{current_user.name} has left!\n\n')


@socketio.on('store_message')
def store_message(text):
    message = f'{current_user.name}: {text}'
    new_message = Chat(data=message)

    db.session.add(new_message)
    db.session.commit()


@socketio.on('send_message')
def send_message(text):
    message = f'{current_user.name}: {text}'
    emit('receive_message', message, broadcast=True)
