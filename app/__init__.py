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
login.login_view = 'login' # tell flask-login which view handles logins

# create database stuff
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# add packages
from app.auth import blueprint as auth_bp
app.register_blueprint(auth_bp)

# add main routes
from app.main import blueprint as main_bp
app.register_blueprint(main_bp)

# importing models
from .models import *

if __name__ == '__main__':
	app.run()
