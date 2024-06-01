from flask import Blueprint
from src.config import chat_config
from flask import request
import os
from src.chat import chat
import json

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
    return 'Welcome to API Route'

@api.route('/get_config')
def get_config():
    return vars(chat_config)

@api.route('/set_config', methods=['POST'])
def set_config():
    data = request.get_json()
    chat_config.update(data)
    return 'Config updated successfully'

@api.route('/get_audio_list')
def get_audio_list():
    filenames = os.listdir('dist')
    arr = []
    for n in filenames:
        if n.endswith('.wav'):
            arr.append('.'.join(n.split('.')[:-1]))
    return {'audioList': arr}

@api.route('/new_chat', methods=['POST'])
def new_chat():
    text = json.loads(request.get_data())['text']
    uid = chat.new_chat(text=text)
    print(uid)
    return {'uid': str(uid)}
