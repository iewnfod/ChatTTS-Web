from flask import Blueprint
from src.config import chat_config
from flask import request
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
