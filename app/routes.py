import requests as r
from app import app
from flask import render_template, request
from .services import get_ricks_image 
from .services import get_ricks_name
from .services import get_mortys_image
from .services import get_mortys_name
from .services import get_chars_image
from .services import get_chars_name
from .forms import SearchForm




@app.route('/')
def home():
    headline = 'welcome to the many worlds or Rick & Morty'
    description = 'Rick and Morty is the Emmy award-winning half-hour animated hit comedy series on Adult Swim that follows a sociopathic genius scientist who drags his inherently timid grandson on insanely dangerous adventures across the universe.'
    return render_template('index.html', headline = headline, description = description)

@app.route('/characters')
def characters():
    chars_name = get_chars_name()
    chars = get_chars_image()
    print(chars)
    return render_template('/chars.html', chars=chars, chars_name=chars_name)

@app.route('/rick')
def Ricks():
    ricks_name = get_ricks_name()
    ricks = get_ricks_image()
    print(ricks)
    return render_template('rick.html', ricks=ricks, ricks_name=ricks_name)

@app.route('/morty')
def mortys():
    mortys_name = get_mortys_name()
    mortys = get_mortys_image()
    print(mortys)
    return render_template('morty.html', mortys=mortys, mortys_name=mortys_name )

@app.route('/search', methods=['GET', 'POST'])
def char_search():
    form = SearchForm()
    if request.method == 'POST':
        data = r.get('https://rickandmortyapi.com/api/character/{form.charactername.data}.json').json()
        if data['results']['total'] != '0':
            character = data['results'][0]['image']
        else:
            character = None
        return render_template('search.html', form=form, character=character)
    return render_template('search.html', form=form, character=None)






