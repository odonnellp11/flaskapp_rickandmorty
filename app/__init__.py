from flask import Flask
from flask_login import LOGIN_MESSAGE_CATEGORY
from config import Config

from .auth.routes import auth

from .models import db, login
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth)



db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please sign in to see this page.'
login.login_message_category = 'danger'


from . import routes
from . import models