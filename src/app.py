from flask import Flask, send_file
from src.api import api
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_dir = os.path.join(
	project_dir,
	'frontend',
	'dist'
)

@app.route('/')
def index():
	return send_file(os.path.join(static_dir, 'index.html'))

@app.route('/<p>')
def resources(p):
	f = os.path.join(static_dir, p)
	if os.path.exists(f):
		return send_file(f)
	else:
		return f'{p} not exist', 404

@app.route('/assets/<p>')
def assets(p):
	f = os.path.join(static_dir, 'assets', p)
	if os.path.exists(f):
		return send_file(f)
	else:
		return f'assets/{p} not exist', 404

@app.route('/audio/<uid>')
def audio(uid):
	f = os.path.join(project_dir, 'dist', f'{uid}.wav')
	if os.path.exists(f):
		return send_file(f)
	else:
		return f'audio/{uid} not exist', 404

app.register_blueprint(api)
