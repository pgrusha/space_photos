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


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    for number, url in enumerate(response.json()['links']['flickr']['original']):
        download_image(url, 'spacex{}.jpg'.format(number + 1))    


