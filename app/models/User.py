from app import db
from flask_login import UserMixin
from app import login # thats the LoginManager

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class Garage(db.Model):
	garage_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer)
	car_id = db.Column(db.Integer)

	def __repr__(self):
		return '<userid={}, carid={}>'.format(self.user_id, self.car_id)
