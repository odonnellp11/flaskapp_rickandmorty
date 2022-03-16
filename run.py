from app import app
from app import db, User

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User}