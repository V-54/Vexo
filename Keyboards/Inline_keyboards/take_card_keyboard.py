from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def send_quession_keyboard():
    take_card_quession_keyboard = InlineKeyboardMarkup()
    yes_btn = InlineKeyboardButton(text="Yes", callback_data="yes")
    no_btn = InlineKeyboardButton(text="No", callback_data="no")
    take_card_quession_keyboard.add(yes_btn, no_btn)
    return take_card_quession_keyboard
