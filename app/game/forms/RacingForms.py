from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import ValidationError, InputRequired, Email, EqualTo

from app.game.data.enviroment_data import tracks, tyres
from app.game.data.car_data import allcars

ERRMSG_SELECT_NEEDED = "Please select at least one of the following."

class RaceStartForm(FlaskForm):

	track_choices = [(track.id, track.getDescription()) for track in tracks.values() if not track.testOnly]
	tyre_choices = [(tyre.id, tyre.name) for tyre in tyres.values()]
	car_choices = [(car.id, car.getCompleteDesc()) for car in allcars.values()]


	track_select = RadioField('Track Select', choices=track_choices, validators=[InputRequired(message=ERRMSG_SELECT_NEEDED)])
	car_select = RadioField('Car Select', choices=car_choices, validators=[InputRequired(message=ERRMSG_SELECT_NEEDED)])
	tyre_select = RadioField('Tyre Select', choices=tyre_choices, validators=[InputRequired(message=ERRMSG_SELECT_NEEDED)])
	submit = SubmitField('Start racing')
