from flask import render_template
from app import app
import time

@app.route("/")
@app.route("/index")
def hello_world():
	return render_template('main.html', timestamp=time.time())

@app.route("/user/<name>")
def display_user(name):
	# A string of any length(without slashes) can be assigned to the variable name.
	return "Your name is {}".format(name)
