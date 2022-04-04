from distutils.log import debug
from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/people")
def users():
    return {"users": ["jason", "john ", "jose"]}


@app.route("/logcheck", methods = ["GET"])
def checker():
    given = request.get_json
    print(given)
    #username = given["user"]
    #pswd = given["pswd"]

    return{
        "lastname": "asdasdasd"
    }


if __name__ == "__main__":
    app.run(debug=True)
