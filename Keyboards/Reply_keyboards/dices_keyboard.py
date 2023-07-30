from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def dices_keyboard():
    dice_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    d4 = KeyboardButton('/rd4')
    d6 = KeyboardButton('/rd6')
    d8 = KeyboardButton('/rd8')
    d10 = KeyboardButton('/rd10')
    d12 = KeyboardButton('/rd12')
    d20 = KeyboardButton('/rd20')
    back_btn = KeyboardButton('/Main_Menu')
    dice_keyboard.add(d4, d6, d8, d10, d12, d20, back_btn)
    return dice_keyboard


def roll_dice_4():
    d4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d4 = KeyboardButton('/1d4')
    c2_d4 = KeyboardButton('/2d4')
    c3_d4 = KeyboardButton('/3d4')
    c4_d4 = KeyboardButton('/4d4')
    c5_d4 = KeyboardButton('/5d4')
    c6_d4 = KeyboardButton('/6d4')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d4_keyboard.add(c1_d4, c2_d4, c3_d4, c4_d4, c5_d4, c6_d4, dice_list, back_btn)
    return d4_keyboard


def roll_dice_6():
    d6_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d6 = KeyboardButton('/1d6')
    c2_d6 = KeyboardButton('/2d6')
    c3_d6 = KeyboardButton('/3d6')
    c4_d6 = KeyboardButton('/4d6')
    c5_d6 = KeyboardButton('/5d6')
    c6_d6 = KeyboardButton('/6d6')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d6_keyboard.add(c1_d6, c2_d6, c3_d6, c4_d6, c5_d6, c6_d6, dice_list, back_btn)
    return d6_keyboard


def roll_dice_8():
    d8_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d8 = KeyboardButton('/1d8')
    c2_d8 = KeyboardButton('/2d8')
    c3_d8 = KeyboardButton('/3d8')
    c4_d8 = KeyboardButton('/4d8')
    c5_d8 = KeyboardButton('/5d8')
    c6_d8 = KeyboardButton('/6d8')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d8_keyboard.add(c1_d8, c2_d8, c3_d8, c4_d8, c5_d8, c6_d8, dice_list, back_btn)
    return d8_keyboard


def roll_dice_10():
    d10_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d10 = KeyboardButton('/1d10')
    c2_d10 = KeyboardButton('/2d10')
    c3_d10 = KeyboardButton('/3d10')
    c4_d10 = KeyboardButton('/4d10')
    c5_d10 = KeyboardButton('/5d10')
    c6_d10 = KeyboardButton('/6d10')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d10_keyboard.add(c1_d10, c2_d10, c3_d10, c4_d10, c5_d10, c6_d10, dice_list, back_btn)
    return d10_keyboard


def roll_dice_12():
    d12_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d12 = KeyboardButton('/1d12')
    c2_d12 = KeyboardButton('/2d12')
    c3_d12 = KeyboardButton('/3d12')
    c4_d12 = KeyboardButton('/4d12')
    c5_d12 = KeyboardButton('/5d12')
    c6_d12 = KeyboardButton('/6d12')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d12_keyboard.add(c1_d12, c2_d12, c3_d12, c4_d12, c5_d12, c6_d12, dice_list, back_btn)
    return d12_keyboard


def roll_dice_20():
    d20_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d20 = KeyboardButton('/1d20')
    c2_d20 = KeyboardButton('/2d20')
    c3_d20 = KeyboardButton('/3d20')
    c4_d20 = KeyboardButton('/4d20')
    c5_d20 = KeyboardButton('/5d20')
    c6_d20 = KeyboardButton('/6d20')
    back_btn = KeyboardButton('/Main_Menu')
    dice_list = KeyboardButton('/dices')
    d20_keyboard.add(c1_d20, c2_d20, c3_d20, c4_d20, c5_d20, c6_d20, dice_list, back_btn)
    return d20_keyboard
