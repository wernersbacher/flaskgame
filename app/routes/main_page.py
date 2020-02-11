from flask import render_template
from app import app
import time

@app.route("/")
@app.route("/index")
def index():
	return render_template('main.html', timestamp=time.time())
