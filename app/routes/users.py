from flask import render_template
from app import app
from app.forms.users import LoginForm


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('users/login.html', title='Sign In', form=form)