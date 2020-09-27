from flask_app import db, bcrypt, login_manager
from flask_login import UserMixin
from datetime import date


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    sets = db.relationship('MovementSet', backref = 'user', lazy=True)

    def __repr__(self):
        return f'User({self.username}'

    def get_id(self):
        return self.user_id

    @classmethod
    def create_user(cls, username, email, password):
        hashed_password = bcrypt.generate_password_hash(
            password=password
        ).decode('utf-8')
        user = cls(username=username, password=hashed_password, email=email)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def check_repetitive_credentials(cls, username, email):
        repetitive_username = cls.query.filter_by(username=username).first()
        repetitive_email = cls.query.filter_by(email=email).first()

        if repetitive_username:
            raise Exception(
                'Username already taken. Please choose another one.'
            )
        if repetitive_email:
            raise Exception(
                'Email already taken. Please another email.')

    @classmethod
    def get_by_credentials(cls, email, password):
        user = cls.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user


class MovementSet(db.Model):
    movement_set_id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id'),
        nullable=False
    )
    movements = db.relationship('Movement', backref='set', lazy=True)


    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()


    @classmethod
    def create_set(cls, user_id, set_name):
        set = cls(user_id=user_id, set_name=set_name)
        db.session.add(set)
        db.session.commit()


class Movement(db.Model):
    """A specific movement belongs to a set and has repetition time and number of movement."""
    movement_id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(
        db.Integer,
        db.ForeignKey('movement_set.movement_set_id'),
        nullable=False
    )
    name = db.Column(db.String, nullable=False)
    repetitions = db.relationship('Repetition', backref = 'movement', lazy=True)
    actions = db.relationship('MovementAction', backref = 'movement', lazy=True)

    @classmethod
    def find_for_set(cls, set_id):
        return cls.query.filter_by(set_id=set_id).all()

    @classmethod
    def create_movement(cls, name, set_id):
        movement = Movement(name=name, set_id=set_id)
        db.session.add(movement)
        db.session.commit()

    @classmethod
    def delete_movement(cls, movement_id):
        """."""
        movement = cls.query.filter_by(movement_id=movement_id).first()

        for repetition in movement.repetitions:
            db.session.delete(repetition)
        for action in movement.actions:
            db.session.delete(action)
        db.session.delete(movement)
        db.session.commit()


class Repetition(db.Model):
    """This is a model for simulating movement repetitions."""
    repetition_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.movement_id'))

    @classmethod
    def create_repetition(cls, number, movement_id):
        db.session.add(cls(number=number, movement_id=movement_id))
        db.session.commit()


class MovementAction(db.Model):
    """The movements which have been implemented by a body builder."""
    movement_action_id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.movement_id'))
    repetition = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)


    @classmethod
    def create_action(cls, movement_id, repetition, weight):
        """Creates an action."""
        db.session.add(
            cls(
                movement_id=movement_id,
                repetition=repetition,
                weight=weight,
                date=date.today()
            )
        )
        db.session.commit()


    @classmethod
    def get_by_movement(cls, movement_id):
        """Returns all the actions for a specific movement."""
        return cls.query.filter_by(movement_id=movement_id).all()




