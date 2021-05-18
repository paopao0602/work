# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import subprocess
from flask import Flask, render_template, url_for, make_response, request
import socket
import sys
import os
import time
HOSTNAME=socket.gethostname()
app = Flask(__name__)
@app.route('/')
def index():
    print(request.headers)
    response = make_response("Here, take some cookie!")
    response.headers["Set-Cookie"] = "user=e2e"
    print(response.headers)
    return response
@app.route('/path_10')
def path10():
    return "Hello from ServerTimeout_10 !".format(HOSTNAME)
@app.route('/path_20')
def path20():
    return "Hello from ServerTimeout_20 !".format(HOSTNAME)
@app.route('/path_60')
def path60():
    return "Hello from ServerTimeout_60 !".format(HOSTNAME)
if __name__ == '__main__':
    app.run( host="0.0.0.0", port=int(sys.argv[1]))
