from app import db
from app.models import User

def get_users():
    return User.query.all()

def add_user_to_db(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
