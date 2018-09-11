# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import render_template
import sys, logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

count = 0

@app.route("/")
def hello():
    return "Hello World"

@app.route("/integration-test")
def integration_test():
    global count
    if count < 2018:
        count = count + 1
    print 'INFO Incoming Testing ' + str(count) + ' from User-Agent: ' + request.headers['User-Agent']
    return "Receiving Request..."

@app.route("/countdown")
def countdown():
    return render_template('it.html', year=str(count))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
