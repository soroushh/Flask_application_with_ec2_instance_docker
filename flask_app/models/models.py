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



