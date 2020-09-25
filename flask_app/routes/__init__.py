from flask import render_template, flash, redirect, url_for
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm
from flask_app.models.models import User


@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            User.check_repetitive_credentials(
                username=form.username.data,
                email=form.email.data
            )
            User.create_user(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data
            )
            flash(
                message='Your account created, you are able to login.',
                category='success'
            )
            return redirect(url_for('log_in'))
        except Exception:
            flash(message=str(Exception.value), category='danger')

    return render_template('register.html', titile='register', form=form)


@app.route('/login',methods=['GET', 'POST'])
def log_in():
    form = LoginForm()

    if form.validate_on_submit():
        flash(
            message='Logged in successfully.',
            category='success'
        )
        return redirect(url_for('home'))

    return render_template('login.html', titile='Log in', form=form)
