from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def blackjack_keyboard_set():
    blackjack_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    score_btn = KeyboardButton('/score')
    Play_BJ_btn = KeyboardButton('/PlayBJ')
    Bet_btn = KeyboardButton('/Bet')
    back_games_btn = KeyboardButton('/games')
    back_btn = KeyboardButton('/Main_Menu')
    blackjack_keyboard.add(
        score_btn,
        Play_BJ_btn,
        Bet_btn,
        back_games_btn,
        back_btn
    )
    return blackjack_keyboard
