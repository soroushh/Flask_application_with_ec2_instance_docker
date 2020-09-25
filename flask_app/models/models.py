from flask_app import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

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




