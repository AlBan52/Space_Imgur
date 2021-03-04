import os
import requests
import urllib3
from dotenv import load_dotenv


urllib3.disable_warnings()


def get_hubble_images_ids():

    payload = {'page': 'all', 'collection_name': 'spacecraft'}
    response = requests.get(
        'http://hubblesite.org/api/v3/images', params=payload)
    response.raise_for_status()
    image_files_descriptions = response.json()
    images_ids = [image['id'] for image in image_files_descriptions]

    return images_ids


def download_hubble_images_link(image_id):

    get_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(get_url)
    response.raise_for_status()
    image_files_descriptions = response.json()['image_files']
    image_link = image_files_descriptions[-1]['file_url']

    return image_link


def download_hubble_images(file_path, image_link, image_id, image_exten):

    response = requests.get(f'http:{image_link}', verify=False)
    response.raise_for_status()
    with open(f'{file_path}/{image_id}{image_exten}', 'wb') as file:
        file.write(response.content)
        print(f'Downloading image: {image_id}{image_exten}')


if __name__ == '__main__':

    load_dotenv()
    file_path = os.getenv('IMAGES')
    os.makedirs(file_path, exist_ok=True)

    images_ids = get_hubble_images_ids()
    print('Downloading hubbles images start...')
    for image_id in images_ids:
        image_link = download_hubble_images_link(image_id)
        name_link, image_exten = os.path.splitext(image_link)
        download_hubble_images(file_path, image_link, image_id, image_exten)
    print('Downloading hubbles images is done')
