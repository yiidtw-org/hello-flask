# -*- coding: utf-8 -*-
from flask import Flask, request
import sys, logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Tuesday"

@app.route("/integration-test")
def integration_test():
    print 'INFO Incoming Hello from User-Agent: ' + request.headers['User-Agent']
    return "Got You"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
