import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'

def get_cat_img():
    response = requests.get(CAT_API)
    response.raise_for_status()

    data = response.json()
    img_cat = data[0]['url']

    return img_cat