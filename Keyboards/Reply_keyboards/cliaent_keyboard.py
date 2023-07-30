from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard_set():
    main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    dice_btn = KeyboardButton('/dices')
    games_btn = KeyboardButton('/games')
    settings_btn = KeyboardButton('/settings')
    main_keyboard.add(
        dice_btn,
        games_btn,
        settings_btn
    )
    return main_keyboard


def settings_menu_set():
    settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_btn = KeyboardButton('/admin')
    language_btn = KeyboardButton('/language')
    about_btn = KeyboardButton('/about')
    back_btn = KeyboardButton('/Main_Menu')
    settings_keyboard.add(
        admin_btn,
        about_btn,
        language_btn,
        back_btn
    )
    return settings_keyboard


def games_menu_set():
    games_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    dice_btn = KeyboardButton('/dice')
    slot_btn = KeyboardButton('/slot')
    bowling_btn = KeyboardButton('/bowling')
    dart_btn = KeyboardButton('/dart')
    blackjack_btn = KeyboardButton('/BlackJack')
    back_btn = KeyboardButton('/Main_Menu')
    games_keyboard.add(
        dice_btn,
        slot_btn,
        bowling_btn,
        dart_btn,
        blackjack_btn,
        back_btn
    )
    return games_keyboard
