from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_db_cursor():
	my_db = mysql.connector.connect(
	host= os.environ.get('DB_SERVER'),
	user= os.environ.get('USER_NAME'),
	password= os.environ.get('PASS_WORD'),
	database = os.environ.get('DB_NAME'),
	port=3306
	)
	my_cursor = my_db.cursor()
	return my_db, my_cursor
