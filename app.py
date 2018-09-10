# -*- coding: utf-8 -*-
from flask import Flask
from datetime import datetime
import sys, logging

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/var/log/hello-flask/app.log", "a") as f:
        f.write("INFO " + now + " Logging Test\n")
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
