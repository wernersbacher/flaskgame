from flask import render_template, Blueprint

import time

main_page = Blueprint('main_page', __name__)

@main_page.route("/")
def hello_world():
	return render_template('main.html', timestamp=time.time())

@main_page.route("/user/<name>")
def display_user(name):
	# A string of any length(without slashes) can be assigned to the variable name.

	return "Your name is {}".format(name)
