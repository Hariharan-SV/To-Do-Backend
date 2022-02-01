from flask import Flask	
app = Flask(__name__)

@app.route('/', methods = ['GET'])	
def hello():
	return 'HELLO'

@app.route('/login', methods = ['GET'])	
def login():
	return 'LOGIN'
