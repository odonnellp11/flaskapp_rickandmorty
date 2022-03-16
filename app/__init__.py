from flask import Flask
from config import Config
from . import routes



app = Flask(__name__)
app.config.from_object(Config)






