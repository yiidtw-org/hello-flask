# -*- coding: utf-8 -*-
from flask import Flask
import sys, logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("hello world logging")
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('/var/log/hello-flask/app.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
       '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)s %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

    app.run(host='0.0.0.0', port=8080)
