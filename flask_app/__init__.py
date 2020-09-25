from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soroush'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://soroush:kati8212579@soroush-database.cvgmzutcx9w8.eu-west-1.rds.amazonaws.com/postgres"
db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
login_manager = LoginManager(app=app)


@app.route('/')
@app.route('/ping')
@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/home')
def home():
    return render_template("home.html", title='Home')


