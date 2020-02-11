from app import db

class Garage(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	car_id = db.Column(db.Integer)

	def __repr__(self):
		return '<userid={}, carid={}>'.format(self.user_id, self.car_id)
