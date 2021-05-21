# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import subprocess
from flask import Flask, render_template, url_for, make_response, request
import socket
import sys
import os
import time
HOSTNAME=socket.gethostname()
# ip_address = socket.gethostbyname(HOSTNAME)
ip_address = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
app = Flask(__name__)
@app.route('/')
def index():
    print(request.headers)
    response = make_response("Here, take some https cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user_https=e2e_https"
    print(response.headers)
    return response
@app.route('/temp1')
def temp1():
    print(request.headers)
    response = make_response("https:temp1 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user1_https=temp1_https"
    print(response.headers)
    return response
@app.route('/temp2')
def temp2():
    print(request.headers)
    response = make_response("https:temp2 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user2_https=temp2_https"
    print(response.headers)
    return response
@app.route('/temp3')
def temp3():
    print(request.headers)
    response = make_response("https:temp3 cookie from "+ip_address)
    response.headers["Set-Cookie"] = "user3_https=temp3_https"
    print(response.headers)
    return response
if __name__ == '__main__':
    app.run( host="0.0.0.0", port=int(sys.argv[1]),ssl_context='adhoc')