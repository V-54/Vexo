from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def send_about_keyboard():
    about_link_keyboard = InlineKeyboardMarkup()
    URL_btn = InlineKeyboardButton(text="Open GitHub",
                                   url="https://github.com/V-54/Vexo")
    about_link_keyboard.add(URL_btn)
    return about_link_keyboard
