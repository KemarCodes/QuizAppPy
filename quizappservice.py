from flask import Flask, request
from user import User

import jwt
import json

app = Flask(__name__)

@app.route('/user/login',methods=['POST'])
def getUser():
    requestData = request.get_json()
    userName = requestData['name']
    print("userName:" + userName)
    usr = User().getUserByName(userName)[0]
    print(usr[0])
    res = {"name": usr[1]}
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algoritm="HS256")
    test = {"id": 2,
        "name": "bill",
        "email": "bill@example.com",
        "access_token": encoded_jwt,
        "expires_in": 360}
    return json.dumps(test)

if __name__ == "__main__":
    app.run()