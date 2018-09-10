# -*- coding: utf-8 -*-
from flask import Flask, request
import sys, logging

app = Flask(__name__)

count = 0

@app.route("/")
def hello():
    return "Hello World"

@app.route("/integration-test")
def integration_test():
    global count
    count = count + 1
    print 'INFO Incoming Testing ' + str(count) + ' from User-Agent: ' + request.headers['User-Agent']
    return "DevOpsDay " + str(count)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
