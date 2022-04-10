from distutils.log import debug
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
#from users import Users
import sys


app = Flask(__name__)
CORS(app)
client = PyMongo(app, uri="mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
# password is TEST123 for jrd
# pass word is helloworld for tester
db = client.db
userCollec = db.users


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods=["POST", "GET"])
def checker():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']

    newDoc = {
        "username": usernameParam,
        "password": pswrdParam
    }

    found = False

    for person in userCollec.find({},{ "_id": 0, "username": 1, "password": 1 }):
        if(person['username'] == usernameParam):
            found = True

    # check if exists in db 
    #TO

    return{
        "message": "approved"
    }


@app.route("/adduser", methods=["POST", "GET"])  # get and post
def addPerson():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']

    newDoc = {
        "username": usernameParam,
        "password": pswrdParam
    }

    # check if the user is in database, if not add it
    #TODOooooooooo PLEASE FIX asdasdasdsssdasdsdlll__________________________________________
    #__________________________________________________________
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


if __name__ == "__main__":
    app.run(debug=True)
