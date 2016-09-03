from flask import Flask, request, redirect, render_template, session, flash

import re
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
