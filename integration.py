import flask
import os
from flask import request, send_from_directory
from sqlalchemy import null
from GettingRequestFromClient import GettingRequestFromClient

app = flask.Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    get_object_on_server = GettingRequestFromClient(request)
    if get_object_on_server != null:
        a = get_object_on_server.run_server_program()
    return a.__str__() 

if __name__ == "__main__":
    #
    app.run()