from flask import render_template
from flask_app import app, db
from flask_app.models.person import Person


@app.route('/people')
def people():
    person = Person(name='soroush', family='khosravi', age=29)
    db.session.add(person)
    db.session.commit()
    return 'Person created completely.'

@app.route('/all_people')
def all_people():
    all_people = Person.query.all()
    return render_template('all.html', people=all_people)
