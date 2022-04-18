from distutils.log import debug
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from encrypt import customEncrypt
from databaseImplementation import database
from dataApi import scrape
from projectImplement import projectMan
import random
import json
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

#dbVar = database()

projVar = projectMan()


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}

@app.route("/idlist", methods=["POST", "GET"])
def gettingids():
    given = request.get_json()
    isHw = given['isHw']
    message = projVar.getIdsStr(isHw)
    return{
        "message": message
    }

@app.route("/apiaccess", methods=["POST", "GET"])
def scrapData():
    given = request.get_json()
    link1 = given['link1']
    link2 = given['link2']
    link3 = given['link3']
    link4 = given['link4']
    link5 = given['link5']
    cite1 = scrape(link1)
    cite2 = scrape(link2)
    cite3 = scrape(link3)
    cite4 = scrape(link4)
    cite5 = scrape(link5)

    return{
        "meta1" : cite1,
        "meta2": cite2,
        "meta3": cite3,
        "meta4": cite4,
        "meta5": cite5,
        "message": "approved"

    }





@app.route("/logcheck", methods=["POST", "GET"])
def checker():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']

    found = False
    

    for person in userCollec.find({},{ "_id": 0, "username": 1, "password": 1, "n": 1}):
        nval = person['n']
        testUser = customEncrypt(person['username'], nval, -1)
        if(testUser == usernameParam):
            testPassword = customEncrypt(person['password'], nval, -1)
            if(testPassword == pswrdParam):
                found = True
        

    if(found):
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
    userToInsert = customEncrypt(usernameParam, nval, 1)
    passToInsert = customEncrypt(pswrdParam, nval, 1)
    

    newDoc = {
        "username": userToInsert,
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

    for person in userCollec.find({},{ "_id": 0, "username": 1, "password": 1 , "n": 1 }):
        tempn = person['n']
        testUser = customEncrypt(person['username'], tempn, -1)
        if(testUser == usernameParam):
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
    isHw = 0
    ids = given["id"]
    response = "default response"
    response = projVar.createProj(isHw, name, descript, ids)

    return{
        "message": response
    }

    

@app.route("/checkProj", methods=["POST", "GET"])
def checkerProj():
    given = request.get_json()
    ids = given["id"]
    reponseFromDb = projVar.checkExistence(ids)

    #this method will check if proj exists then return approved if its good
    return {
        "message": reponseFromDb
    }


@app.route("/bigloader", methods=["POST", "GET"])
def loading():
    given = request.get_json()
    ids = given["id"]
    responseFromDb = projVar.getStatus(ids)

    return responseFromDb

@app.route("/inorout", methods=["POST", "GET"])
def movesets():
    given = request.get_json()
    qty = given['qty']
    ids = given['id']
    hwsetname = given['hwsetname']
    type = given['check']
    result = 0
    if(type == "checkin"):
       result =  projVar.checkin(qty, ids, hwsetname)
    else:
        result = projVar.checkout(qty, ids, hwsetname)

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
