from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

MIN_USERNAME_LENGTH = 2
MAX_USERNAME_LENGTH = 20

class RegistrationForm(FlaskForm):
    """The class enabling users to sign up"""
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=MIN_USERNAME_LENGTH, max=MAX_USERNAME_LENGTH)
        ]
    )
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """The class enabling users to Log in."""
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


class MovementSetForm(FlaskForm):
    """This class enables users to create a new MovementSet."""
    set_name = StringField('Set Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MovementForm(FlaskForm):
    """This class helps us to create new movements."""
    movement_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RepetitionForm(FlaskForm):
    """This class helps you to define the movement's repetition."""
    number = IntegerField('Number of repetion', validators=[DataRequired()])
    submit = SubmitField('Submit')



