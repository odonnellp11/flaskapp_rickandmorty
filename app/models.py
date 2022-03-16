# responsible for everything datadase
#creation of database models (tables/ entities)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4
from flask_login import LoginManager, UserMixin


db = SQLAlchemy()



@login.user_loader
def load_user(user_id):
    return user.query.get(user_id)





class User(db.Models, UserMixin):
    id = db.column(db.integer, primary_key=True)
    username = db.column(db.string(15), nullable=False, unique=True)
    email = db.column(db.string(50), nullable=False, unique=True)
    first_name = db.column(db.string(50)
    last_name = db.column(db.string(50)
    password = db.column(db.string(50), nullable= False)
    date_created = db.column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, first_name='', Last_name='')
        self.username = username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password)
        self.id = str(uuid4())