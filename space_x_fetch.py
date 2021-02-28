import os
import requests


def fetch_image_links_spacex_last_launch():

    get_url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(get_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']

    return images_links


def download_images_spacex_last_launch(images_links):

    for image_number, image_link in enumerate(images_links):
        response = requests.get(image_link)
        response.raise_for_status()
        with open(f'{file_path}/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)
        print(f'Downloading spase-X images: spacex_{image_number}.jpg')
    print('Downloading spase-X images is done')


if __name__ == '__main__':

    file_path = 'd:/CODING/DEVMAN/Space_Imgur/images'
    os.makedirs(file_path, exist_ok=True)

    images_links = fetch_image_links_spacex_last_launch()
    download_images_spacex_last_launch(images_links)
