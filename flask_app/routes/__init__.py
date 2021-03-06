from flask import render_template, flash, redirect, url_for, request
from flask_app import app
from flask_app.forms import (
    RegistrationForm, LoginForm, MovementSetForm, MovementForm, RepetitionForm,
    MovementActionFrom
)
from flask_app.models.models import (
    User, MovementSet, Movement, Repetition, MovementAction
)
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
        except Exception as error:
            flash(message=str(error), category='danger')

    return render_template('register.html', titile='register', form=form)


@app.route('/login',methods=['GET', 'POST'])
def log_in():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        if User.get_by_credentials(
            email=form.email.data, password=form.password.data
        ):
            user = User.get_by_credentials(
                email=form.email.data, password=form.password.data
            )
            login_user(user=user, remember=form.remember.data)

            if request.args.get('next'):
                return redirect(request.args.get('next'))
            return redirect(url_for('home'))
        else:
            flash(
                message='Login unsuccessful, please check email and password.',
                category='danger'
            )

    return render_template('login.html', titile='Log in', form=form)


@app.route('/logout')
def logout():
    """."""
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    """."""
    return render_template('account.html', titile='Account')

@app.route('/ping')
@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/home')
@app.route('/')
@login_required
def home():
    return render_template("home.html", title='Home')


@app.route('/sets')
@login_required
def sets():
    """Shows the movement sets to the user."""
    user_id = current_user.user_id

    sets = MovementSet.find_by_user_id(user_id=user_id)

    return render_template('sets.html', sets=sets)

@app.route('/sets/add', methods=['GET', 'POST'])
@login_required
def create_set():
    """Creates a set for a specific user."""
    form = MovementSetForm()

    if form.validate_on_submit():
        MovementSet.create_set(
            user_id=current_user.user_id,
            set_name=form.set_name.data
        )
        flash('Set successfully created.', 'success')
        return redirect(url_for('sets'))

    return render_template('create_set.html', form=form)


@app.route('/sets/<int:set_id>/movements')
def movements(set_id):
    """The function shows the movements related to a specific set."""
    movements = Movement.find_for_set(set_id=set_id)

    return render_template('movements.html', movements=movements, set_id=set_id)


@app.route('/sets/<int:set_id>/movement',methods=['GET', 'POST'])
def create_movement(set_id):
    """The view function enabling us to create a movement"""
    form = MovementForm()

    if form.validate_on_submit():
        Movement.create_movement(name=form.movement_name.data, set_id=set_id)
        flash('Movement successfully added', 'success')
        return redirect(url_for('movements', set_id=set_id))

    return render_template('create_movement.html', form=form)


@app.route(
    '/sets/<int:set_id>/movement/<int:movement_id>/repetition',
    methods=['GET', 'POST']
)
def create_repetition(set_id, movement_id):
    form = RepetitionForm()

    if form.validate_on_submit():
        Repetition.create_repetition(
            number=form.number.data,
            movement_id=movement_id
        )
        flash('Repetition successfully added', 'success')
        return redirect(url_for('movements', set_id=set_id))

    return render_template('create_repetition.html', form=form)


@app.route('/sets/<int:set_id>/movement/<int:movement_id>/remove')
def delete_movement(set_id, movement_id):
    Movement.delete_movement(movement_id=movement_id)
    flash('Movement successfully deleted', 'success')
    return redirect(url_for('movements', set_id=set_id))


@app.route(
    '/set/<int:set_id>/movement/<int:movement_id>/action/create',
    methods=['GET', 'POST']
)
def create_action(set_id, movement_id):
    form = MovementActionFrom()

    if form.validate_on_submit():
        MovementAction.create_action(
            movement_id=movement_id,
            weight=form.weight.data,
            repetition=form.repetition.data
        )
        flash('Action successfully submitted.', 'success')
        return redirect(url_for('movements', set_id=set_id))

    return render_template('create_action.html', form=form)


@app.route('/set/<int:set_id>/movement/<int:movement_id>/actions')
def get_actions(set_id, movement_id):
    actions = MovementAction.get_by_movement(movement_id=movement_id)

    return render_template(
        'action_history.html',
        actions=actions,
        set_id=set_id
    )










