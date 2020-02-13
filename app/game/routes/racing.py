from flask import render_template, flash, redirect, url_for, request
from app import db
from app.game import bp
from app.game.forms.RacingForms import RaceStartForm
from app.models import User
# login stuff
from flask_login import current_user, login_user
from flask_login import logout_user
from werkzeug.urls import url_parse
# db stuff
from app.models.User import User

# game logic
from app.game.logic.racing import getResult

@bp.route('/racing', methods=['GET', 'POST'])
def racing():
	form = RaceStartForm()
	if form.validate_on_submit():

		#print(form.tyre_select.data, form.car_select.data, form.track_select.data)

		time_taken, tyres_used = getResult(trackid=form.track_select.data, carid=form.car_select.data, tyreid=form.tyre_select.data)

		result_message = f"You finished in {time_taken:.2f}s and used {tyres_used*100:.2f}% of your tyres."
		flash(result_message)

	return render_template('game/racing/overview.html', title='Go Racing!', form=form)
