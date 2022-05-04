from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_menu(products):
    inline_keyboard = [
        [InlineKeyboardButton(product['name'], callback_data=product['id'])] for product in products
    ]
    inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)

    return inline_kb_markup


def get_description_menu():
    inline_keyboard = [
        [
            InlineKeyboardButton('1 кг', callback_data=1),
            InlineKeyboardButton('5 кг', callback_data=5),
            InlineKeyboardButton('10 кг', callback_data=10)
        ],
        [InlineKeyboardButton('Назад', callback_data='back')],
        [InlineKeyboardButton('Корзина', callback_data='cart')],
    ]
    inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)

    return inline_kb_markup
