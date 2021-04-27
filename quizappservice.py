from flask import Flask, request
from flask_cors import cross_origin
from user import User
from studyset import StudySet

import jwt
import json

app = Flask(__name__)


@app.route('/user/login',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def getUser():
    requestData = request.get_json()
    userEmail = requestData['email']
    userPassword = requestData['password']
    print(" Email:" + userEmail + " Password:" + userPassword)
    usr = User().getUserByEmailAddress(userEmail)[0]
    sessionID = str(User().createSession(usr[0])[0][0])
    print("SessionID: " + sessionID)
    encoded_jwt = jwt.encode({"some": "payload"}, sessionID, algorithm="HS256")
    if(usr[3] == userPassword):
        authResponse = {
            "id": usr[0],
            "name": usr[1],
            "email": usr[2],
            "access_token": encoded_jwt.decode(),
            "expires_in": 18000
        }
        User().updateSessionToken(sessionID, encoded_jwt.decode())
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
@cross_origin(headers=['Content-Type'])
def addUser():
    requestData = request.get_json()
    userName = requestData['name']
    userEmail = requestData['email']
    userPassword = requestData['password']
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
    sessionID = str(User().createSession(usr[0])[0][0])
    encoded_jwt = jwt.encode({"some": "payload"}, sessionID, algorithm="HS256")
    User().updateSessionToken(sessionID, encoded_jwt.decode())
    authResponse = {
        "id": usr[0],
        "name": usr[1],
        "email": usr[2],
        "access_token": encoded_jwt.decode(),
        "expires_in": 18000
    }
    return json.dumps(authResponse)

    
@app.route('/study/studysets',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def retrieveStudySets():
    requestData = request.get_json()
    sessionToken = requestData['sessionToken']
    print("retrieveStudySets - sessionToken:" + sessionToken)
    #should be checking if the sessionToken is even valid first
    userID = User().getUserIDBySessionToken(sessionToken)[0][1]
    studySetList = StudySet().getStudySetByUserID(userID) 
    sslen = len(studySetList)
    count = 0
    rs = '{"studysets": ['
    for i in studySetList:
        rs = rs + '{"id": ' + str(i[0]) + ', "name": "' + str(i[2]) + '"}'
        #The logic should work for sets with multiple entries, but might break
        #if they have none
        count = count + 1
        if(count < sslen):
            rs = rs + ','
    rs = rs + ']}'
    print(rs)
    return rs

@app.route('/study/terms',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def retrieveTerms():
    requestData = request.get_json()
    studySetID = requestData['studySetID']
    print("retrieveTerms - studySetID:" + studySetID)
    #should be checking the sessionToken is even valid first
    termList = StudySet().getTermsByStudySetID(studySetID)
    sslen = len(termList)
    count = 0
    rs = '{"terms": ['
    for i in termList:
        rs = rs + '{"study_set_name": "' + str(i[0]) \
        + '", "term": "' + str(i[1]) \
        + '", "description": "' + str(i[2]) \
        + '", "term_id": ' + str(i[3]) \
        + ', "study_set_id": ' + str(i[4]) \
        + '}'
        #The logic should work for sets with multiple entries, but might break
        #if they have none
        count = count + 1
        if(count < sslen):
            rs = rs + ','
    rs = rs + ']}'
    print(rs)
    return rs

@app.route('/study/newterm',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def addTerm():
    requestData = request.get_json()
    studySetID = requestData['studySetID']
    term = requestData['term']
    description = requestData['description']
    print("newTerm - studySetID:" + studySetID\
        + " term:" + term + " description: " + description)
    #should be checking the sessionToken is even valid first
    StudySet().addTerm(studySetID, term, description)
    termList = StudySet().getTermsByStudySetID(studySetID)
    sslen = len(termList)
    count = 0
    rs = '{"terms": ['
    for i in termList:
        rs = rs + '{"study_set_name": "' + str(i[0]) \
        + '", "term": "' + str(i[1]) \
        + '", "description": "' + str(i[2]) \
        + '", "term_id": ' + str(i[3]) \
        + ', "study_set_id": ' + str(i[4]) \
        + '}'
        #The logic should work for sets with multiple entries, but might break
        #if they have none
        count = count + 1
        if(count < sslen):
            rs = rs + ','
    rs = rs + ']}'
    print(rs)
    return rs


if __name__ == "__main__":
    app.run()