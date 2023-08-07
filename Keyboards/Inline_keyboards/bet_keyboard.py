from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def bet_keyboard_set():
    bet_keyboard = InlineKeyboardMarkup(row_width=2, one_time=True)
    plus50 = InlineKeyboardButton(text='+50', callback_data='+50')
    plus100 = InlineKeyboardButton(text='+100', callback_data='+100')
    plus250 = InlineKeyboardButton(text='+250', callback_data='+250')
    plus500 = InlineKeyboardButton(text='+500', callback_data='+500')
    minus50 = InlineKeyboardButton(text='-50', callback_data='-50')
    minus100 = InlineKeyboardButton(text='-100', callback_data='-100')
    minus250 = InlineKeyboardButton(text='-250', callback_data='-250')
    minus500 = InlineKeyboardButton(text='-500', callback_data='-500')
    all_in = InlineKeyboardButton(text='all in', callback_data='all')
    bet_keyboard.add(
        plus50,
        minus50,
        plus100,
        minus100,
        plus250,
        minus250,
        plus500,
        minus500,
        all_in
    )
    return bet_keyboard
