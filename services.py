import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'
DUCK_API = 'https://random-d.uk/api/random'
DOG_API = 'https://api.thedogapi.com/v1/images/search'


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

def get_dog_api():
    response = requests.get(DOG_API)
    response.raise_for_status()

    data = response.json()
    img_dog = data[0]['url']

    return img_dog