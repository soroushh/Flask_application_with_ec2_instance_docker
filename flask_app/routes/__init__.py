from flask import render_template
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm


@app.route('/register')
def sign_up():
    form = RegistrationForm()

    return render_template('register.html', titile='register', form=form)


@app.route('/login')
def log_in():
    form = LoginForm()

    return render_template('login.html', titile='Log in', form=form)
