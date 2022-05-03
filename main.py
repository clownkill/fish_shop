import os
from random import choice

import requests
from dotenv import load_dotenv


def get_product_ids(token):
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
    product_ids = [product['id'] for product in products]

    return product_ids


def add_to_cart(token, product_id):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    json_data = {
        'data': {
            'id': product_id,
            'type': 'cart_item',
            'quantity': 1,
        },
    }

    response = requests.post('https://api.moltin.com/v2/carts/abc/items', headers=headers, json=json_data)
    response.raise_for_status()

    print(response.text)


def get_cart(token):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get('https://api.moltin.com/v2/carts/abc', headers=headers)
    print(response.text)


def main():
    load_dotenv()
    shop_token = os.getenv('SHOP_ACCESS_TOKEN')

    # product_ids = get_product_ids(shop_token)

    # add_to_cart(shop_token, choice(product_ids))

    get_cart(shop_token)





if __name__ == '__main__':
    main()