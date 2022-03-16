from re import X
import requests as r



def char_image():
    response = r.get('https://rickandmortyapi.com/api/character/?name=rick')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
   
    chars = []
    for image in data:
        if data[image]:
            chars.append((image, data[image]))
    return chars
