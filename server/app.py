#!/usr/bin/env python3

# import module
from flask import Flask

# instantiate
app = Flask(__name__)


'''
decorator === functions that take functions as arguments and return them decorated with new features.
index is a view
'''
@app.route("/")
def index():
    return "<h1>Welcome to my app!</h1>"


'''
route parameter === in angle brackets
user is a view
'''
@app.route("/<string:username>")
def user(username):
    return f"<h1>Profile for {username}</h1>"


if __name__ == "__main__":
    app.run(port=5555)


'''
OR
export FLASK_APP=app/app.py
export FLASK_RUN_PORT=5555
flask run
'''
 