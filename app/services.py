import requests as r



def char_image():
    response = r.get('https://rickandmortyapi.com/api/character/1')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
   
    chars = []
    for name in data:
        if data[name]:
            chars.append((name, data[name]))
    return chars