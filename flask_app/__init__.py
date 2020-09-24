from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/ping')
def start():
    return 'This is the health endpoint.'
