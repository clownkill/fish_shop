import os

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


def main():
    load_dotenv()
    shop_token = os.getenv('SHOP_ACCESS_TOKEN')

    product_ids = get_product_ids(shop_token)



if __name__ == '__main__':
    main()