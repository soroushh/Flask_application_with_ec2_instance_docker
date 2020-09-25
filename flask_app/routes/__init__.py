from flask import render_template, flash, redirect, url_for
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm


@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(
            message=f'Account created for {form.username.data}.',
            category='success'
        )
        return redirect(url_for('home'))

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
