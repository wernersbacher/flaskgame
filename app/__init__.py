from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# create config
app.config.from_object(Config)

#create database stuff
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# add routes
from .routes.main_page import main_page
app.register_blueprint(main_page)

from .models import *

if __name__ == '__main__':
	app.run()
