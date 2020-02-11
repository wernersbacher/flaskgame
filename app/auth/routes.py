from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.auth.forms import LoginForm, RegistrationForm
# login stuff
from flask_login import current_user, login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

# db stuff
from app.models.User import User


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			# wrong data
			flash('Invalid username or password')
			return redirect(url_for('login'))
		# ok, login
		login_user(user, remember=form.remember_me.data)
		# get back to the last site
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)

	# just show the login template
	return render_template('auth/login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('auth/register.html', title='Register', form=form)
