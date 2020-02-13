from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.game.data.enviroment_data import tracks, tyres
from app.game.data.car_data import allcars


class RaceStartForm(FlaskForm):

	track_choices = [(track.id, track.getDescription()) for track in tracks.values() if not track.testOnly]
	tyre_choices = [(tyre.id, tyre.name) for tyre in tyres.values()]
	car_choices = [(car.id, car.name) for car in allcars.values()]


	track_select = RadioField('Track Select', choices=track_choices, validators=[DataRequired()])
	car_select = RadioField('Car Select', choices=car_choices, validators=[DataRequired()])
	tyre_select = RadioField('Tyre Select', choices=tyre_choices, validators=[DataRequired()])
	submit = SubmitField('Start racing')
