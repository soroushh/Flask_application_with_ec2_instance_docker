from flask_app import app, db
from flask_app.models.person import Person


@app.route('/people')
def people():
    person = Person(name='soroush', family='khosravi', age=29)
    db.session.add(person)
    db.session.commit()
    return 'Person created completely.'
