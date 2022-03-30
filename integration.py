import flask
import os
from flask import request, send_from_directory

app = flask.Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    a = request.args.get('POLICY_ACTION')
    return a

if __name__ == "__main__":
    app.run()