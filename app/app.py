# import logging
# from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse

import fastai
from fastai import vision

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return vision.URLs.MNIST_SAMPLE

app.run()