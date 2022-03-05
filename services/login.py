import bcrypt
import os
import jwt

from db import get_db_cursor


def handle_login(body):
    salt = os.environ.get('SALT')
    _, my_cursor = get_db_cursor()
    my_cursor.execute("SELECT * from Users WHERE email='"+body['email']+"';")
    results = my_cursor.fetchall()
    my_cursor.close()
    if len(results) == 0:
        return { 'status': 'FAILED', 'message': 'User does not exist' }
    if results[0][2] != bcrypt.hashpw(body['password'].encode('utf8'), salt.encode('utf8')).decode():
        return { 'status': 'FAILED', 'message': 'Passwords Mismatch !' }
    return {'status': 'SUCCESS', 'token': jwt.encode({
        'name': results[0][-1],
        'id': results[0][0],
        'email': results[0][1]
    }, os.environ.get('JWT_KEY')) }