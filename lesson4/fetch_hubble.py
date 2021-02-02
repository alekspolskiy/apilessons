import requests
import os


def get_hubble_image(image_id, images_folder):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(url)
    response.raise_for_status()
    collection_name = response.json()['collection']
    file_url = '{}{}'.format('https:', response.json()['image_files'][-1]['file_url'])
    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    with open('{}/{}{}{}'.format(images_folder,
                                 collection_name,
                                 image_id,
                                 os.path.splitext(file_url)[-1]),
              'wb') as file:
        file.write(response.content)


def get_images_from_collection(collection_name, images_folder):
    collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'

    response = requests.get(collection_url)
    response.raise_for_status()
    images_ids = [file_id['id'] for file_id in response.json()]
    for file_id in images_ids:
        get_hubble_image(file_id, images_folder)
