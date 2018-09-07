# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/ola")
def echo():
    return "ola"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
