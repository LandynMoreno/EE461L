from distutils.log import debug
from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
#from users import Users
import sys
import databaseImplementation


app = Flask(__name__)
CORS(app)
currentUserId = ""
client = PyMongo(app, uri="mongodb+srv://tester:helloworld@cluster0.wsoqa.mongodb.net/project?retryWrites=true&w=majority")
# password is TEST123 for jrd
# pass word is helloworld for tester
db = client.db
projCollec = db.Projects


@app.route("/logcheck", methods=["POST", "GET"])
def checker():
    given = request.get_json()
    cap1 = given['capacity1']
    avl1 = given['availability1']
    qty1 = given['quantity1']
    cap2 = given['capacity2']
    avl2 = given['availability2']
    qty2 = given['quantity2']

    newDoc = {
        "capacity1": cap1,
        "availability1": avl1,
        "quantity1": qty1,
        "capacity2": cap2,
        "availability2": avl2,
        "quantity2": qty2
    }

    found = False

    # if project exists
    # message = approved
    # then update all db/hw sets
    # for project in projCollec.find({}, {"ids": ids})


if __name__ == "__main__":
    app.run(debug=True)
