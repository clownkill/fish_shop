import os
from pprint import pprint

import requests
from dotenv import load_dotenv


def get_token(client_id):
    url = 'https://api.moltin.com/oauth/access_token'
    data = {
        'client_id': client_id,
        'grant_type': 'implicit'
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    token = response.json()['access_token']

    return token


def get_products(token):
    url = 'https://api.moltin.com/v2/products/'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(
        url,
        headers=headers
    )
    response.raise_for_status()
    shop_data = response.json()

    products = shop_data['data']

    return products


def get_product(token, product_id):
    url = f'https://api.moltin.com/v2/products/{product_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(
        url,
        headers=headers
    )
    response.raise_for_status()
    product = response.json()

    return product['data']


def get_product_image(token, product_data):
    image_id = product_data['relationships']['main_image']['data']['id']
    url = f'https://api.moltin.com/v2/files/{image_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(
        url,
        headers=headers
    )
    response.raise_for_status()
    product_files = response.json()
    image_url = product_files['data']['link']['href']

    image = requests.get(image_url)
    image.raise_for_status()

    return image_url


def add_to_cart(token, product_id, cart_id, quantity):
    url = f'https://api.moltin.com/v2/carts/{cart_id}/items'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    json_data = {
        'data': {
            'id': product_id,
            'type': 'cart_item',
            'quantity': quantity,
        },
    }

    response = requests.post(
        url,
        headers=headers,
        json=json_data
    )
    response.raise_for_status()

    pprint(response.text)


def get_cart(token):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get('https://api.moltin.com/v2/carts/abc', headers=headers)
    print(response.text)


def main():
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')

    token = get_token(client_id)

    # product_ids = get_product_ids(shop_token)

    # add_to_cart(shop_token, choice(product_ids))

    get_cart(token)


if __name__ == '__main__':
    main()
