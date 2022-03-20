import re
from flask import Blueprint, render_template 

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/')
def signin():
    return render_template('signin.html')


@auth.route('/register')
def signup():
    return render_template('signup.html')