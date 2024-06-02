from flask import Blueprint
from src.config import chat_config
from flask import request
import os
from src.chat import chat
import json
from src.functions import *

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
    return 'Welcome to API Route'

@api.route('/get_config')
def get_config():
    return vars(chat_config)

@api.route('/get_audio_list')
def get_audio_list():
    if not os.path.exists(audio_save_dir):
        os.makedirs(audio_save_dir)
    filenames = os.listdir(audio_save_dir)
    arr = []
    for n in filenames:
        if n.endswith('.wav'):
            arr.append('.'.join(n.split('.')[:-1]))
    return {'audioList': arr}

@api.route('/new_chat', methods=['POST'])
def new_chat():
    data = json.loads(request.get_data())
    text = data['text']
    new_chat_config = data['new_chat_config']
    uid = chat.new_chat(text=text, new_chat_config=new_chat_config)
    return {'uid': str(uid)}

@api.route('/remove_chat/<uid>')
def remove_chat(uid):
    u = chat.remove_chat(uid)
    return {'uid': u}

@api.route('/get_audio_text/<uid>')
def get_audio_text(uid):
    return {'text': get_text_from_uid(uid)}
