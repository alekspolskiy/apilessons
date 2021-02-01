import requests
import os


def get_hubble_image(image_id, images_folder):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(url)
    response.raise_for_status()
    file_url = '{}{}'.format('https:', [image_files['file_url'] for image_files in response.json()['image_files']][-1])

    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    with open('{}/{}{}'.format(images_folder, image_id, os.path.splitext(file_url)[-1]), 'wb') as file:
        file.write(response.content)


def get_images_from_collection(collection_name, images_folder):
    collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'

    response = requests.get(collection_url)
    response.raise_for_status()
    images_id = [file_id['id'] for file_id in response.json()]
    print(images_id)
    for file_id in images_id:
        response = requests.get(f'http://hubblesite.org/api/v3/image/{file_id}')
        response.raise_for_status()
        file_url = '{}{}'.format('https:',
                                 [image_files['file_url'] for image_files in response.json()['image_files']][-1])
        response = requests.get(file_url, verify=False)
        response.raise_for_status()
        with open('{}/{}{}{}'.format(images_folder,
                                     collection_name,
                                     file_id,
                                     os.path.splitext(file_url)[-1]
                                     ), 'wb') as file:
            file.write(response.content)
