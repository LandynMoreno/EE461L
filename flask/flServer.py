from distutils.log import debug
from flask import Flask, render_template, request, redirect
from flask_cors import CORS;
from pymongo import MongoClient


client = MongoClient("mongodb+srv://jrd4455:PASSWORD@cluster0.wsoqa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#password is TEST123
db = client["project"]
users = db["users"]

app = Flask(__name__)
CORS(app)


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods = ["POST"])
def checker():
    given = request.get_json


    return{
        "approval": "approved"
    }


if __name__ == "__main__":
    app.run(debug=True)
