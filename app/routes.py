from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/characters')
def characters():
    return render_template('char.html')

@app.route('/rick')
def Ricks():
    return render_template('/rick.html')

@app.route('/morty')
def mortys():
    return render_template('/morty.html')
