# -*- coding: utf-8 -*-
from flask import Flask, request
import sys, logging

app = Flask(__name__)

@app.route("/")
def hello():
    print 'INFO Incoming Hello from User-Agent: ' + request.headers['User-Agent']
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
