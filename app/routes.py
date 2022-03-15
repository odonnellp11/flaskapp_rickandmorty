from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/charaters')
def characters():
    return render_template('char.html')