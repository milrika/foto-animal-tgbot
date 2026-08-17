import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'
DUCK_API = 'https://random-d.uk/api/random'

def get_cat_img():
    response = requests.get(CAT_API)
    response.raise_for_status()

    data = response.json()
    img_cat = data[0]['url']

    return img_cat

def get_duck_img():
    response = requests.get(DUCK_API)
    response.raise_for_status()

    data = response.json()
    img_duck = data['url']

    return img_duck