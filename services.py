import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'
DUCK_API = 'https://random-d.uk/api/random'
DOG_API = 'https://api.thedogapi.com/v1/images/search'
TAXIK_API = 'https://dog.ceo/api/breed/dachshund/images/random'


def get_cat_img():
    try:
        response = requests.get(CAT_API)
        response.raise_for_status()

        data = response.json()
        img_cat = data[0]['url']

        return img_cat

    except Exception as e:
        print(f'ошибка {e}')
        return None

def get_duck_img():
    try:
        response = requests.get(DUCK_API)
        response.raise_for_status()

        data = response.json()
        img_duck = data['url']

        return img_duck

    except Exception as e:
        print(f'ошибка {e}')
        return None

def get_dog_img():
    try:
        response = requests.get(DOG_API)
        response.raise_for_status()

        data = response.json()
        img_dog = data[0]['url']

        return img_dog

    except Exception as e:
        print(f'ошибка {e}')
        return None

def get_taxik_img():
    try:
        response = requests.get(TAXIK_API)
        response.raise_for_status()

        data = response.json()
        img_taxik = data['message']

        return img_taxik 
    
    except Exception as e:
        print(f'ошибка {e}')
        return None
