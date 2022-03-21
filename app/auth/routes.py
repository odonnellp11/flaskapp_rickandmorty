from re import I
from flask import Blueprint, render_template , request, redirect, url_for, flash
from flask_login import login_user, logout_user
auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')
from .auth_forms import SignInForm, RegisterForm 
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required



@auth.route('/', methods=['GET', 'POST'])
def signin():
    siform = SignInForm()
    if request.method == 'POST':
        if siform.validate_on_submit():
            user = User.query.filter_by(username=siform.username.data).first()
            if user and check_password_hash(user.password, siform.password.data):
                login_user(user)
                print(current_user, current_user.__dict__)
            
                flash(f'Welcome back to Rick & Morty world, { current_user.first_name }!!! ')
                return redirect(url_for('home'))
        flash(f'Login Failed, Try Again')
        return redirect(url_for('auth.signin'))
    return render_template('signin.html', siform=siform)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            newuser = User(rform.username.data, rform.email.data, rform.password.data, rform.first_name.data, rform.last_name.data)
            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash(f'Username or Email is already in use. Try Again', category='danger')
                return redirect(url_for('auth.register'))
            login_user(newuser)
            flash(f'Registration Complete!!! Welcome {rform.first_name.data}!',category='success')
            return redirect(url_for('home'))
        else:
            flash('Password not valid', category='danger')
            return redirect(url_for('auth.register'))
    return render_template('register.html', rform=rform)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!!!', category='info')
    return redirect(url_for('auth.signin'))