from flask import Flask
from config import Config
# extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
# create config
app.config.from_object(Config)

# add login manager
login = LoginManager(app)

# create database stuff
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# add routes
from .routes.main_page import main_page
app.register_blueprint(main_page)

# importing models
from .models import *

if __name__ == '__main__':
	app.run()
