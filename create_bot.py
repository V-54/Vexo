from aiogram import Dispatcher, Bot

from Data.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)