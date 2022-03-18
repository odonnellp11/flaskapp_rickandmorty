from re import X
import requests as r


# api calls for ricks page
def get_ricks_image():
    response = r.get('https://rickandmortyapi.com/api/character/?name=rick')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    ricks=[]
    for i in range(len(data['results'])):
        if data['results'][i]['image']:
            ricks.append((i, data['results'][i]['image']))                                                                               #ricks[data['results'][i]['name']] = data['results'][i]['image']
    return ricks


def get_ricks_name():
    response = r.get('https://rickandmortyapi.com/api/character/?name=rick')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    ricks_name=[] 
    for i in range(len(data['results'])):
        if data['results'][i]['name']:
            ricks_name.append((i, data['results'][i]['name']))
    return ricks_name



#api calls for mortys page
def get_mortys_image():
    response = r.get('https://rickandmortyapi.com/api/character/?name=morty')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    mortys=[]
    for i in range(len(data['results'])):
        if data['results'][i]['image']:
            mortys.append((i, data['results'][i]['image']))                                                                               #ricks[data['results'][i]['name']] = data['results'][i]['image']
    return mortys


def get_mortys_name():
    response = r.get('https://rickandmortyapi.com/api/character/?name=morty')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    mortys_name=[] 
    for i in range(len(data['results'])):
        if data['results'][i]['name']:
            mortys_name.append((i, data['results'][i]['name']))
    return mortys_name
       
#api calls for all characters
def get_chars_image():
    response = r.get('https://rickandmortyapi.com/api/character')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    chars=[]
    for i in range(len(data['results'])):
        if data['results'][i]['image']:
            chars.append((i, data['results'][i]['image']))                                                                               #ricks[data['results'][i]['name']] = data['results'][i]['image']
    return chars


def get_chars_name():
    response = r.get('https://rickandmortyapi.com/api/character')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    chars_name=[] 
    for i in range(len(data['results'])):
        if data['results'][i]['name']:
            chars_name.append((i, data['results'][i]['name']))
    return chars_name
       
