from flask import Flask
from config import Config
# extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


# add login manager
login = LoginManager()
login.login_view = 'auth.login' # tell flask-login which view handles logins

# create database stuff
db = SQLAlchemy()
migrate = Migrate()

bootstrap = Bootstrap()

def create_app(config_class=Config):

	app = Flask(__name__)
	# create config
	app.config.from_object(config_class)

	login.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	bootstrap.init_app(app)

	# add packages
	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp)

	# add main routes
	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	# add game routes
	from app.game import bp as game_bp
	app.register_blueprint(game_bp, url_prefix='/game')

	return app


# importing models
from .models import User
