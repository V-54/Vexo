import time
import random

from aiogram import types

import threading

from create_bot import bot
from Data.Text_messages import dice_messages
from Keyboards.Reply_keyboards.dices_keyboard import *

lock = threading.Lock()


async def send_dices_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.DICE, reply_markup=dices_keyboard())


async def send_d4_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD4_LIST, reply_markup=roll_dice_4())


async def send_d6_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD6_LIST, reply_markup=roll_dice_6())


async def send_d8_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD8_LIST, reply_markup=roll_dice_8())


async def send_d10_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD10_LIST, reply_markup=roll_dice_10())


async def send_d12_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD12_LIST, reply_markup=roll_dice_12())

async def send_d20_keyboard(message: types.Message):
    await message.delete()
    await message.answer(dice_messages.RD20_LIST, reply_markup=roll_dice_20())


async def roll_dice(message: types.Message):
    await message.delete()
    await message.answer('Wait please...')
    number = int(message.text[1])
    if len(message.text) == 5:
        dice_facet = int(message.text[3] + message.text[4])
    else:
        dice_facet = int(message.text[3])
    i = 0
    try:
        while i < number:
            await bot.send_chat_action(message.chat.id, 'typing')
            lock.locked()
            i += 1
            roll_dice = str(random.randint(1, dice_facet))
            await bot.send_message(message.chat.id,
                                   str(i) + f'{dice_messages.TEXT_RD}{dice_facet} =  {roll_dice}')
        lock.release()
        time.sleep(2)
    except:
        # чтобы не было ошибок при спаме
        # бот ждет, пока прошлая команда завершится
        time.sleep(3)


def register_handlers_dice(dp):
    dp.register_message_handler(send_d4_keyboard, commands=['rd4'])
    dp.register_message_handler(send_d6_keyboard, commands=['rd6'])
    dp.register_message_handler(send_d8_keyboard, commands=['rd8'])
    dp.register_message_handler(send_d10_keyboard, commands=['rd10'])
    dp.register_message_handler(send_d12_keyboard, commands=['rd12'])
    dp.register_message_handler(send_d20_keyboard, commands=['rd20'])
    dp.register_message_handler(send_dices_keyboard, commands=['dices'])
    dp.register_message_handler(roll_dice, commands=['1d4', '2d4', '3d4', '4d4', '5d4', '6d4',
                                                     '1d6', '2d6', '3d6', '4d6', '5d6', '6d6',
                                                     '1d8', '2d8', '3d8', '4d8', '5d8', '6d8',
                                                     '1d10', '2d10', '3d10', '4d10', '5d10', '6d10',
                                                     '1d12', '2d12', '3d12', '4d12', '5d12', '6d12',
                                                     '1d20', '2d20', '3d20', '4d20', '5d20', '6d20'])
