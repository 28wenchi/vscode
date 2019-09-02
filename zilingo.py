import os
from hashlib import md5
# from multiprocessing import Pool
from urllib.parse import urlencode

import re
import requests


def get_page(offset):
    params = {
        'sort_order': 'popular',
        'screen_type': 'sub_category',
        'screen_id': 'KGITOP',
        'zl_a_st': 'sub_category',
        'zl_a_si': 'KGITOP',
        'zl_a_pid': 'SCR-1561468078442-5e6f927c-e3d2-4f6a-a50a-8391bfc33287',
        'after': offset
    }
    url = 'https://zilingo.com/en-sg/Baby-and-Kids/Girls/Tops?sort_order=popular' + urlencode(
        params)
    try:
        response = requests.get(url)
        print(url)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError:
        return None


"""
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            print(type(title))
            images = item.get('image_list')
            print(type(images))
            for image in images:
                # yield {'image': image.get('url'), 'title': title}
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                    'image': origin_image,
                    # 'iamge': image.get('url'),
                    'title': title
                }


"""


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                    'image': origin_image,
                    # 'iamge': image.get('url'),
                    'title': title
                }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status.code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                             md5(response.content).hexdigest(),
                                             'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save image')


def main(offset):
    json = get_page(offset)
    get_images(json)
    for item in get_images(json):
        print(item)
        # save_image(item)


if __name__ == '__main__':
    main(48)
"""
GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
"""
