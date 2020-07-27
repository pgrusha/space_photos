import requests
import os
from PIL import Image

def download_image(image_url, image_filename):
    directory = 'images'
    full_path = '{}/{}'.format(directory, image_filename)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    response = requests.get(image_url)
    response.raise_for_status()
    with open(full_path, 'wb') as file:
        file.write(response.content)
    image = Image.open(full_path)
    image.thumbnail((1080, 1080))
    image = image.convert("RGB")
    image.save('{}/{}.jpg'.format(directory, image_filename.split('.')[0]), format="JPEG")


def get_extention(url):
    return url.split('.')[-1]


def fetch_hubble_image(image_id):
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(image_id))
    response.raise_for_status()
    image_url = response.json()['image_files'][-1]['file_url']
    download_image('https:{}'.format(image_url),
                   '{}.{}'.format(image_id, get_extention(image_url)))


def fetch_hubble_collection(collection_name):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    response.raise_for_status()
    for image_info in response.json():
        fetch_hubble_image(image_info['id'])
