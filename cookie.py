# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import subprocess
from flask import Flask, render_template, url_for, make_response, request
import socket
import sys
import os
import time
HOSTNAME=socket.gethostname()
ip_address = socket.gethostbyname(HOSTNAME)
app = Flask(__name__)
@app.route('/')
def index():
    print(request.headers)
    response = make_response("Here, take some http cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user_http=e2e_http"
    print(response.headers)
    return response
@app.route('/temp1')
def temp1():
    print(request.headers)
    response = make_response("http:temp1 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user1_http=temp1_http"
    print(response.headers)
    return response
@app.route('/temp2')
def temp2():
    print(request.headers)
    response = make_response("http:temp2 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user2_http=temp2_http"
    print(response.headers)
    return response
@app.route('/temp3')
def temp3():
    print(request.headers)
    response = make_response("http:temp3 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user3_http=temp3_http"
    print(response.headers)
    return response
if __name__ == '__main__':
    app.run( host="0.0.0.0", port=int(sys.argv[1]))
