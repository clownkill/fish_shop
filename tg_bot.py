import os
import logging
import redis

from dotenv import load_dotenv
from telegram.ext import Filters, Updater
from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler

from keyboard import get_main_menu, get_description_menu
from shop import (get_token, get_products,
                  get_product, get_product_image,
                  add_to_cart,)

_database = None
_product_id = None


def start(bot, update):
    update.message.reply_text(
        'Please choose:',
        reply_markup=get_main_menu(products)
    )

    return 'HANDLE_MENU'


def handle_menu(bot, update):
    query = update.callback_query
    global _product_id
    _product_id = query.data
    product_data = get_product(shop_token, _product_id)
    product_name = product_data['name']
    product_weight = product_data['weight']['kg']
    product_price = product_data['meta']['display_price']['with_tax']['formatted']
    product_description = product_data['description']

    message = f'''
    {product_name}
    {product_price} per {product_weight} kg
    {product_description}
    '''
    image_url = get_product_image(shop_token, product_data)

    bot.send_photo(
        chat_id=query.message.chat_id,
        photo=open('dorado.jpg', 'rb'), # photo=image_url,
        caption=message,
        reply_markup=get_description_menu()
    )

    bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )

    return 'HANDLE_DESCRIPTION'


def handle_description(bot, update):
    query = update.callback_query
    if query.data == 'back':
        bot.send_message(
            chat_id=query.message.chat_id,
            text='Please choose:',
            reply_markup=get_main_menu(products)
        )
        bot.delete_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        return 'HANDLE_MENU'
    elif query.data in ('1', '5', '10'):
        add_to_cart(
            token=shop_token,
            product_id=_product_id,
            cart_id=query.message.from_user['id'],
            quantity=int(query.data)
        )
        return 'HANDLE_DESCRIPTION'



def handle_users_reply(bot, update):
    db = get_database_connection()
    if update.message:
        user_reply = update.message.text
        chat_id = update.message.chat_id
    elif update.callback_query:
        user_reply = update.callback_query.data
        chat_id = update.callback_query.message.chat_id
    else:
        return
    if user_reply == '/start':
        user_state = 'START'
    else:
        user_state = db.get(chat_id)

    states_functions = {
        'START': start,
        'HANDLE_MENU': handle_menu,
        'HANDLE_DESCRIPTION': handle_description,
    }
    state_handler = states_functions[user_state]
    # Если вы вдруг не заметите, что python-telegram-bot перехватывает ошибки.
    # Оставляю этот try...except, чтобы код не падал молча.
    # Этот фрагмент можно переписать.
    try:
        next_state = state_handler(bot, update)
        db.set(chat_id, next_state)
    except Exception as err:
        print(err)


def get_database_connection():
    """
    Возвращает конекшн с базой данных Redis, либо создаёт новый, если он ещё не создан.
    """
    global _database
    if _database is None:
        database_password = os.getenv("DATABASE_PASSWORD")
        database_host = os.getenv("DATABASE_HOST")
        database_port = os.getenv("DATABASE_PORT")
        _database = redis.Redis(
            host=database_host,
            port=database_port,
            password=database_password,
            decode_responses=True,
        )
    return _database


if __name__ == '__main__':
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    tg_token = os.getenv("TELEGRAM_TOKEN")

    shop_token = get_token(client_id)
    products = get_products(shop_token)

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CallbackQueryHandler(handle_users_reply))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_users_reply))
    dispatcher.add_handler(CommandHandler('start', handle_users_reply))
    updater.start_polling()
