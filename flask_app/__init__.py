from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soroush'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://soroush:kati8212579@soroush-database.cvgmzutcx9w8.eu-west-1.rds.amazonaws.com/postgres"
db = SQLAlchemy(app=app)

@app.route('/')
@app.route('/ping')
def start():
    return 'This is the health endpoint.'

@app.route('/home')
def home():
    return render_template("home.html", title='Home')
