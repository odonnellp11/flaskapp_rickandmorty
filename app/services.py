from re import X
import requests as r



def get_ricks_image():
    response = r.get('https://rickandmortyapi.com/api/character/?name=rick')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    ricks={} 
    for i in data:
        if data['results'][0]['image']:
            ricks[i] = data['results'][0]['image']                                           #data['results'][0]['name']
    return ricks


       
