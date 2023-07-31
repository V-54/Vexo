from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def bet_keyboard_set():
    bet_keyboard = InlineKeyboardMarkup(row_width=2, one_time=True)
    plus50 = InlineKeyboardButton(text='+50', callback_data='+50')
    plus100 = InlineKeyboardButton(text='+100', callback_data='+100')
    minus50 = InlineKeyboardButton(text='-50', callback_data='-50')
    minus100 = InlineKeyboardButton(text='-100', callback_data='-100')
    bet_keyboard.add(plus50, plus100, minus50, minus100)
    return bet_keyboard
