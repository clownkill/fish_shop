from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_menu(products):
    inline_keyboard = [
        [InlineKeyboardButton(product['name'], callback_data=product['id'])] for product in products
    ]
    inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)

    return inline_kb_markup


def get_back_btn():
    inline_keyboard = [[InlineKeyboardButton('Назад', callback_data='back')]]
    inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)

    return inline_kb_markup
