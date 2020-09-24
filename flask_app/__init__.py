from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soroush'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app=app)

@app.route('/')
@app.route('/ping')
def start():
    return 'This is the health endpoint.'

@app.route('/home')
def home():
    return render_template("home.html")
