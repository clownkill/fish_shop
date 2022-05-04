import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

from shop import get_token, get_products


def get_inline_keyboard(products):
    inline_keyboard = [
        [InlineKeyboardButton(product['name'], callback_data=product['id'])] for product in products
    ]
    inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)

    return inline_kb_markup

if __name__ == '__main__':
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    token = get_token(client_id, client_secret)
    products = get_products(token)

    get_inline_keyboard()