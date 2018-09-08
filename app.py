# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("hello world logging")
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
