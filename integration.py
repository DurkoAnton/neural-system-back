import flask
import os
from flask import request, send_from_directory

app = flask.Flask(__name__)

@app.route('/', methods = ['POST'])
def home():
    a = request.form['POLICY_ACTION']
    return a

if __name__ == "__main__":
    app.run()