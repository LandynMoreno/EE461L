from distutils.log import debug
from flask import Flask, render_template, request, redirect
from flask_cors import CORS;
from flask_pymongo import PyMongo
from users import Users




app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb+srv://jrd4455:sadfsadf@cluster0.wsoqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#password is TEST123
db = client["project"]
users = db["users"]

@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods = ["POST"])
def checker():
    given = request.get_json


    return{
        "message": "approved"
    }

@app.route("/adduser", methods = ["PUT"]) #get and post
def addPerson():
    #given = request.get_json

    db1 = users.User()
    #db1.addUser(given["username"], given["password"])

    newDoc = {
        "username": "asdasd",
        "password": "asdasda"
    }

    #users.insert_one(newDoc)


    return{
        "message": "approved"
    }


if __name__ == "__main__":
    app.run(debug=True)
