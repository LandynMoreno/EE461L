from distutils.log import debug
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS;
from flask_pymongo import PyMongo
from users import Users




app = Flask(__name__)
CORS(app)
client = PyMongo(app, uri="mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
#password is TEST123 for jrd
db = client.db
userCollec = db.users


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods = ["POST"])
def checker():
    given = request.get_json


    return{
        "message": "approved"
    }

@app.route("/adduser", methods = ["POST", "GET"]) #get and post
def addPerson():
    given = request.get_json()
    usernameParam = given['username']
    pswrdParam = given['password']



    #db1 = users.User()
    #db1.addUser(given["username"], given["password"])

    newDoc = {
        "username": usernameParam,
        "password": pswrdParam
    }

    userCollec.insert_one(newDoc)


    return{
        "message": "asdasd"
    }


if __name__ == "__main__":
    app.run(debug=True)
