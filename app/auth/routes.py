
from flask import Blueprint, render_template , request, redirect, url_for, flash

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

from .auth_forms import SignInForm, RegisterForm 

@auth.route('/', methods=['GET', 'POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':
        if siform.validate_on_submit():
            print(siform.data)
            flash(f'Welcome { siform.username.data } back to Rick & Morty world!!! ')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed, Try Again')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', siform=siform)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            print(rform.data)
            flash(f'Registration Successful!!! Welcome { rform.first_name.data } to Rick & Morty world!!! ')
            return redirect(url_for('home'))
        else:
            flash('Password not valid')
            return redirect(url_for('auth.register'))
    return render_template('register.html', rform=rform)

