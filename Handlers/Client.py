import asyncio

from aiogram import types

from create_bot import bot

from Data.Text_messages import client_messages
from Data_base.users_base import add_user

from Keyboards.Reply_keyboards.cliaent_keyboard import main_keyboard_set, settings_menu_set, games_menu_set
from Keyboards.Inline_keyboards.about_keyboard import send_about_keyboard


async def delete_message(chat_id, message_id):
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


async def send_start_message(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer("🖤")
    await asyncio.sleep(2)
    await delete_message(message.chat.id, message.message_id + 1)
    await message.answer("😈")
    await asyncio.sleep(3)
    await delete_message(message.chat.id, message.message_id + 2)
    await message.answer("👹")
    await asyncio.sleep(2)
    await delete_message(message.chat.id, message.message_id + 3)
    await add_user(message.from_user.username, message.from_user.full_name, message.chat.id, 'ru', 250)
    await message.answer(text=client_messages.TEXT_WARNING_FOR_USERS, parse_mode='markdown')
    await message.answer(text=f"Hello <b>@{message.from_user.username}</b>!", parse_mode='HTML',
                         reply_markup=main_keyboard_set())


async def send_main_menu_message(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer(text=client_messages.TEXT_ASK, reply_markup=main_keyboard_set())


async def help_message(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer(text=client_messages.TEXT_HELP, parse_mode='HTML')


async def settings_message(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer(text=client_messages.TEXT_SETTINGS, parse_mode='HTML', reply_markup=settings_menu_set())


async def games_message(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer(text=client_messages.TEXT_GAMES_LIST, parse_mode='HTML', reply_markup=games_menu_set())


async def send_about_info(message: types.Message):
    await delete_message(message.chat.id, message.message_id)
    await message.answer(client_messages.TEXT_ABOUT, reply_markup=send_about_keyboard())


def register_handlers_client(dp):
    dp.register_message_handler(send_start_message, commands="start")
    dp.register_message_handler(send_main_menu_message, commands="Main_Menu")
    dp.register_message_handler(help_message, commands="help")
    dp.register_message_handler(send_about_info, commands="about")
    dp.register_message_handler(settings_message, commands="settings")
    dp.register_message_handler(games_message, commands="games")
