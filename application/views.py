from application import app
from flask import render_template, jsonify, request, redirect, url_for, session, flash
import os, datetime, time
from flask import session, redirect, url_for, flash
from functools import wraps
# from application.lib.mtcmis import *


@app.route("/")
def home():
    return render_template('index.html')