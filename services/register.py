from dotenv import load_dotenv
import os
import bcrypt

from db import get_db_cursor

load_dotenv()

def handle_register(body):
    salt = os.environ.get('SALT')
    hashed_password = bcrypt.hashpw(body['password'].encode('utf8'), salt.encode('utf-8'))
    my_db, my_cursor = get_db_cursor()
    my_cursor.execute("SELECT * from Users WHERE email = '"+body['email']+"';")
    results = my_cursor.fetchall()
    my_cursor.close()
    my_cursor = my_db.cursor()
    if len(results) > 0:
        return {'status' : 'FAILED', 'message': 'User already exists'}
    query = "INSERT INTO Users(email,password,username) VALUES('"+body['email']+"','"+hashed_password.decode()+"','"+body['name']+"');"
    my_cursor.execute(query)
    my_db.commit()
    my_cursor.close()
    return { 'status' : 'SUCCESS'}