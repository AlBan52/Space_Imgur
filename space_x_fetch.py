import os
import requests
import logging
from dotenv import load_dotenv


def fetch_spacex_last_launch_image_links():

    get_url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(get_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']

    return images_links


def download_spacex_last_launch_images(images_links, file_path):

    for image_number, image_link in enumerate(images_links):
        response = requests.get(image_link)
        response.raise_for_status()
        with open(f'{file_path}/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)
            print(
                f'Downloading spase-X images: spacex_{image_number}.jpg')
    logging.info('Downloading spase-X images is done')


if __name__ == '__main__':

    logging.basicConfig(filename='space_x_fetch.log',
                        filemode='w', level=logging.INFO)
    load_dotenv()
    file_path = os.getenv('IMAGES')
    os.makedirs(file_path, exist_ok=True)

    images_links = fetch_spacex_last_launch_image_links()
    download_spacex_last_launch_images(images_links, file_path)
