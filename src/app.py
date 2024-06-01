from flask import Flask, send_file
from src.api import api
import os

app = Flask(__name__)

static_dir = os.path.join(
	os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
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

app.register_blueprint(api)
