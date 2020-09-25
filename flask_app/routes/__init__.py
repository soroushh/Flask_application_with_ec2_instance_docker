from flask import render_template
from flask_app import app, db
from flask_app.models.models import Person, Movement


@app.route('/people')
def people():
    person = Person(name='soroush', family='khosravi', age=29)
    db.session.add(person)
    db.session.commit()
    return 'Person created completely.'


@app.route('/create/<name>/<family>/<int:age>')
def create_person(name, family, age):
    new_person = Person(name=name, family=family, age=age)
    db.session.add(new_person)
    db.session.commit()
    return 'Person created successfully.'


@app.route('/all_people')
def all_people():
    all_people = Person.query.all()
    return render_template('all.html', people=all_people)

@app.route('/create_movement/<name>/<int:repetition>/<int:person_id>')
def create_movement(name, repetition,person_id):
    """Creates a movement for a person."""
    movement = Movement(name=name, person_id=person_id, repetition=repetition)
    db.session.add(movement)
    db.session.commit()
    return 'model successfully created.'

