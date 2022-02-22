from flask import Flask, request	
import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector
import bcrypt

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
salt = os.environ.get('SALT')
my_db = mysql.connector.connect(
  host= os.environ.get('DB_SERVER'),
  user= os.environ.get('USER_NAME'),
  password= os.environ.get('PASS_WORD'),
  database = os.environ.get('DB_NAME'),
  port=3306
)
my_cursor = my_db.cursor()

@app.route('/', methods = ['GET'])	
def hello():
	return 'HELLO'

@app.route('/login', methods = ['POST'])	
def login():
	body = request.get_json()
	if 'email' not in body or 'password' not in body:
		return 'Bad request'
	my_cursor.execute("SELECT * from USERS WHERE email = "+body['email']+";")
	results = my_cursor.fetchall()
	print(results)
	return 'LOGIN'+body['username']+' '+body['password']

@app.route('/signup', methods=['POST'])
def signup():
	body = request.get_json()
	if 'email' not in body or 'password' not in body:
		return {'message':'Bad request'}
	hashed_password = bcrypt.hashpw(body['password'], salt)
	my_cursor.execute("SELECT * from USERS WHERE email = "+body['email']+";")
	results = my_cursor.fetchall()
	print(results, hashed_password)
	return { 'message' : 'SUCCESS'}

if __name__ == "__main__":
	app.run(debug=True)
