import os
import requests
import urllib3
import logging
from PIL import Image
from dotenv import load_dotenv
from imgurpython import ImgurClient


def edit_images(file_path, edited_images_path):

    images = os.listdir(file_path)
    for image_number, image in enumerate(images):
        image = Image.open(f'{file_path}/{image}')
        image.thumbnail((1080, 1080))
        image.save(f'{edited_images_path}/{image_number}.jpg', format='JPEG')
        logging.info(f'Editing images: {image_number}.jpg')
    logging.info('Editing images is done')


def get_imgur_tokens(client_id, client_secret):

    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')
    print('Go to the following URL: {0}'.format(authorization_url))
    pin = input('Enter pin code: ')

    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(
        credentials['access_token'], credentials['refresh_token'])

    print('Authentication successful! Check details in the .log file')
    logging.info('Authentication successful! Here are the details:')
    logging.info(' Access token:  {0}'.format(credentials['access_token']))
    logging.info(' Refresh token: {0}'.format(credentials['refresh_token']))
    tokens = [credentials['access_token'], credentials['refresh_token']]

    return tokens


def upload_images_to_imgur(client_id,
                           client_secret,
                           access_token,
                           refresh_token
                           ):

    client = ImgurClient(client_id,
                         client_secret,
                         access_token,
                         refresh_token
                         )
    logging.info("Uploading image... ")
    upload_images = os.listdir(edited_images_path)
    for image_number, image in enumerate(upload_images):
        client.upload_from_path(
            f'{edited_images_path}/{image}', config=None, anon=False)
        logging.info(f'Upload: {image_number}')
    logging.info('Uploading images is done')


if __name__ == '__main__':

    logging.basicConfig(filename='imgur_image_post.log',
                        filemode='w', level=logging.INFO)
    urllib3.disable_warnings()
    load_dotenv()
    file_path = os.getenv('IMAGES')
    edited_images_path = os.getenv('EDITED_IMAGES')
    os.makedirs(edited_images_path, exist_ok=True)

    edit_images(file_path, edited_images_path)

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')

    if not access_token:
        access_token, refresh_token = get_imgur_tokens(client_id,
                                                       client_secret
                                                       )
    else:
        refresh_token = os.getenv('REFRESH_TOKEN')

    upload_images_to_imgur(client_id,
                           client_secret,
                           access_token,
                           refresh_token
                           )
