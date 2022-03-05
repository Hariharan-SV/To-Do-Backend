from flask import Flask, request	
from os.path import join, dirname
from dotenv import load_dotenv
from flask_cors import CORS
import json
from helpers.auth import get_session, token_required

from services.login import handle_login
from services.register import handle_register
from services.todo import handle_todos

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])	
def hello():
	return 'HELLO'

@app.route('/login', methods = ['POST'])	
def login():
	body = json.loads(request.get_data().decode('utf-8'))
	if not body or 'email' not in body or 'password' not in body:
		return {'message':'Bad request'}
	res = handle_login(body)
	return res

@app.route('/register', methods=['POST'])
def signup():
	body = json.loads(request.get_data().decode('utf-8'))
	if not body or 'email' not in body or 'password' not in body or 'name' not in body:
		return {'message':'Bad request'}
	return handle_register(body)

@app.route('/get-session', methods = ['POST'])	
@token_required
def get_session_details(is_authenticated):
	return get_session()

@app.route('/get-todos', methods = ['POST'])
@token_required
def get_todos_for_current_user(is_authenticated):
	if not is_authenticated:
		return { 'status': 'FAILED', 'message': 'token is missing'}
	body = json.loads(request.get_data().decode('utf-8'))
	return handle_todos(body['userDetails'])

if __name__ == "__main__":
	app.run(debug=True)
