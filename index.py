from flask import Flask, url_for, render_template
import time

app = Flask(__name__)

# import routes
from routes.main_page import main_page

app.register_blueprint(main_page)

if __name__ == '__main__':
	app.run()
