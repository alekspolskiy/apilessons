import requests


def get_hubble_image(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(url)
    response.raise_for_status()
    file_url = '{}{}'.format('https:', [image_files['file_url'] for image_files in response.json()['image_files']][-1])

    response = requests.get(file_url, verify=False)
    response.raise_for_status()
    with open('images/{}.{}'.format(image_id, file_url.split('.')[-1]), 'wb') as file:
        file.write(response.content)


def get_image_from_collection(collection_name):
    collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'

    response = requests.get(collection_url)
    response.raise_for_status()
    id_list = [file_id['id'] for file_id in response.json()]
    print(id_list)
    for file_id in id_list:
        response = requests.get(f'http://hubblesite.org/api/v3/image/{file_id}')
        response.raise_for_status()
        file_url = '{}{}'.format('https:',
                                 [image_files['file_url'] for image_files in response.json()['image_files']][-1])
        response = requests.get(file_url, verify=False)
        response.raise_for_status()
        with open('images/{}{}.{}'.format(collection_name,
                                          file_id,
                                          file_url.split('.')[-1]
                                          ), 'wb') as file:
            file.write(response.content)
