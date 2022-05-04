from telegram import InlineKeyboardButton, InlineKeyboardMarkup

inline_keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                    InlineKeyboardButton("Option 2", callback_data='2')],
                   [InlineKeyboardButton("Option 3", callback_data='3')]]

inline_kb_markup = InlineKeyboardMarkup(inline_keyboard)
