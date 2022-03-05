from functools import wraps
from flask import request, jsonify
import jwt, os, json

def token_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = None
    authorized = False
    body = json.loads(request.get_data().decode('utf-8'))
    if 'x-auth-token' in body:
      token = body['x-auth-token']
    if token is not None:
      try:
        jwt.decode(token, os.environ.get('JWT_KEY'), algorithms="HS256")
        authorized = True
      except jwt.ExpiredSignatureError or jwt.InvalidTokenError:
        authorized = False
    return f(authorized,*args, **kwargs)            
  return decorator

def get_session():
	token = None
	data = {"status": "FAILED", "message": "Pending"}
	body = json.loads(request.get_data().decode('utf-8'))
	if 'x-auth-token' in body:
		token = body['x-auth-token']
	if token is None:
		return {"status": "FAILED", "message": "Token is missing !!"}
	try:
		data = jwt.decode(token, os.environ.get('JWT_KEY'), algorithms="HS256")
		data["status"] = "SUCCESS"
	except jwt.ExpiredSignatureError:
		return {"status": "FAILED", "message": "Token is expired !!"}
	except jwt.InvalidTokenError:
		return {"status": "FAILED",  "message": "Token is invalid !!"}
	return jsonify(data)
