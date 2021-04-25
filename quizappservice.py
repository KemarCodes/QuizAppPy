from flask import Flask, request
from user import User

import jwt
import json

app = Flask(__name__)

@app.route('/user/login',methods=['POST'])
def getUser():
    userEmail = request.form.get('email')
    userPassword = request.form.get('password')
    print(" Email:" + userEmail + " Password:" + userPassword)
    usr = User().getUserByEmailAddress(userEmail)[0]
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    if(usr[3] == userPassword):
        authResponse = {
            "id": usr[0],
            "name": usr[1],
            "email": usr[2],
            "access_token": encoded_jwt.decode(),
            "expires_in": 18000
        }
        return json.dumps(authResponse)
    else:
        authResponse = {
            "id": 0,
            "name": "none",
            "email": "none",
            "access_token": "none",
            "expires_in": 0
        }
        return json.dumps(authResponse)

@app.route('/user/register',methods=['POST'])
def addUser():
    userName = request.form('name')
    userEmail = request.form('email')
    userPassword = request.form('password')
    print("Register - Name:" + userName + " Email:" + userEmail\
         + " Password:" + userPassword)   
    if(User().checkIfUserExists(userName, userEmail) == False):
        User().addNewUser(userName, userEmail, userPassword)
    else:
        authResponse = {
            "id": 0,
            "name": "none",
            "email": "none",
            "access_token": "none",
            "expires_in": 0
        }
        return json.dumps(authResponse)
    usr = User().getUserByEmailAddress(userEmail)[0]
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    authResponse = {
        "id": usr[0],
        "name": usr[1],
        "email": usr[2],
        "access_token": encoded_jwt.decode(),
        "expires_in": 18000
    }
    return json.dumps(authResponse)


if __name__ == "__main__":
    app.run()