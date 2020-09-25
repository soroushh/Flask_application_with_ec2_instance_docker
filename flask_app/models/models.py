from flask_app import db, bcrypt

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'User({self.username}'

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




