from distutils.log import debug
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from encrypt import customEncrypt
from databaseImplementation import database
import random
#from users import Users
import sys


app = Flask(__name__)
CORS(app)
currentUserId = ""
client = PyMongo(app, uri="mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
# password is TEST123 for jrd
# pass word is helloworld for tester
db = client.db
userCollec = db.users

dbVar = database()


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods=["POST", "GET"])
def checker():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']

    found = False
    

    for person in userCollec.find({},{ "_id": 0, "username": 1, "password": 1, "n": 1}):
        if(person['username'] == usernameParam):
            nval = person['n']
            testPassword = customEncrypt(person['password'], nval, -1)
            if(testPassword == pswrdParam):
                found = True
        

    if(found):
        currentUserId = usernameParam
        return{
            "message": "approved"
        }
    else:
        return{
            "message": "incorrect login details"
        }



@app.route("/adduser", methods=["POST", "GET"])  # get and post
def addPerson():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']
    nval = random.randint(1,4)
    passToInsert = customEncrypt(pswrdParam, nval, 1)
    

    newDoc = {
        "username": usernameParam,
        "password": passToInsert,
        "n": nval
    }


    if ((' ' in usernameParam) or ('!' in usernameParam)):
        return{
            "message": "Invalid characters used in username"
        }
    if ((' ' in pswrdParam) or ('!' in pswrdParam)):
        return{
            "message": "Invalid characters used in password"
        }

    found = False

    for person in userCollec.find({},{ "_id": 0, "username": 1, "password": 1 }):
        if(person['username'] == usernameParam):
            found = True

    
    if (not found):
        userCollec.insert_one(newDoc)
        return{
            "message": "approved"
        }
    else:
        return{
            "message": "failed, already exists as username"
        } 


@app.route("/projecting", methods=["POST", "GET"])
def projActions():
    #this endpoint will add a project
    # name: projName,
    #             description: projDescrip,
    #             id: projId
    given  = request.get_json()
    name = given["name"]
    descript = given["description"]
    ids = given["id"]
    username = given["username"]
    response = "default response"
    response = dbVar.createdocuments(name, descript, ids, 200, username)

    return{
        "message": response
    }

    

@app.route("/checkProj", methods=["POST", "GET"])
def checkerProj():
    given = request.get_json()
    ids = given["id"]
    username = given['username']
    reponseFromDb = dbVar.checkExists(ids, username)

    #this method will check if proj exists then return approved if its good
    return {
        "message": reponseFromDb
    }


@app.route("/bigloader", methods=["POST", "GET"])
def loading():
    given = request.get_json()
    ids = given["id"]
    username = given["username"]
    responseFromDb = dbVar.getdata(ids, username)
    usersCurHw1 = dbVar.gethwnumbers(ids, username, "hwset1")
    usersCurHw2 = dbVar.gethwnumbers(ids, username, "hwset2")
    responseFromDb["hw1value"] = usersCurHw1
    responseFromDb["hw2value"] = usersCurHw2

    return responseFromDb

@app.route("/inorout", methods=["POST", "GET"])
def movesets():
    given = request.get_json()
    qty = given['qty']
    ids = given['id']
    hwsetname = given['hwsetname']
    username = given['username']
    type = given['check']
    result = 0
    if(type == "checkin"):
       result =  dbVar.checkin(qty, ids, hwsetname, username)
    else:
        result = dbVar.checkout(qty, ids, hwsetname, username)
    
    if(result == -1):
        return {
            "message": "invalid input or other error"
        }
    else:
        return {
            "message": "approved"
        }
    



    return True






if __name__ == "__main__":
    app.run(debug=True)
