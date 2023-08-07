from asyncio import sleep

from aiogram import types

from create_bot import bot
from Data_base.users_base import check_score, update_score


async def send_dice(message: types.message):
    await message.delete()
    if await check_score(message) >= 35:
        dice = await bot.send_dice(message.chat.id, emoji='🎲')
        if dice.dice.value <= 3:
            score = await check_score(message) - 35
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"You lose\n Score - {await check_score(message)}$")
        elif dice.dice.value >= 4:
            score = await check_score(message) + dice.dice.value * 10
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"You <b>win!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
    else:
        await message.answer(f"For play you need 35$\n You have - {await check_score(message)}")
        await sleep(5)
        score = 50
        await update_score(message, score)
        await message.answer("Take it for play <b>+50$</b>", parse_mode='HTML')


# 22- chery; 1 - bar; 64- jackpot;
async def send_slot(message: types.message):
    await message.delete()
    if await check_score(message) >= 30:
        dice = await bot.send_dice(message.chat.id, emoji='🎰')
        if dice.dice.value == 1:
            score = await check_score(message) + 250
            await update_score(message, score)
            await sleep(2)
            await message.answer(f"you have <b>Bar</b>\n <b>Score - {await check_score(message)}$</b>",
                                 parse_mode='HTML')
        elif dice.dice.value == 22:
            score = await check_score(message) + 150
            await update_score(message, score)
            await sleep(2)
            await message.answer(f"you have <b>Chery</b>\n <b>Score - {await check_score(message)}$</b>",
                                 parse_mode='HTML')
        elif dice.dice.value == 64:
            score = await check_score(message) + 777
            await update_score(message, score)
            await sleep(2)
            await message.answer(f"You have <b>Jackpot!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
        else:
            score = await check_score(message) - 30
            await update_score(message, score)
            await sleep(1.5)
            await message.answer(f"You lose\n Score - {await check_score(message)}$")
    else:
        await message.answer(f"For play you need 35$\n You have - {await check_score(message)}")
        await sleep(5)
        score = 50
        await update_score(message, score)
        await message.answer("Take it for play <b>+50$</b>", parse_mode='HTML')


async def send_dart(message: types.message):
    await message.delete()
    if await check_score(message) >= 40:
        dice = await bot.send_dice(message.chat.id, emoji='🎯')
        if dice.dice.value == 1:
            score = await check_score(message) - 40
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"Absolutely by\n Score - {await check_score(message)}$")
        elif 1 < dice.dice.value <= 3:
            score = await check_score(message) - 35
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"You lose\n Score - {await check_score(message)}$")
        elif 4 <= dice.dice.value < 6:
            score = await check_score(message) + dice.dice.value * 10
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"You <b>win!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
        else:
            score = await check_score(message) + 100
            await update_score(message, score)
            await sleep(3)
            await message.answer(f"<b>Exactly!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
    else:
        await message.answer(f"For play you need 35$\n You have - {await check_score(message)}")
        await sleep(5)
        score = 50
        await update_score(message, score)
        await message.answer("Take it for play <b>+50$</b>", parse_mode='HTML')


async def send_bowling(message: types.message):
    await message.delete()
    if await check_score(message) >= 40:
        dice = await bot.send_dice(message.chat.id, emoji='🎳')
        if dice.dice.value == 1:
            score = await check_score(message) - 40
            await update_score(message, score)
            await sleep(3.5)
            await message.answer(f"Absolutely by\n Score - {await check_score(message)}$")
        elif 1 < dice.dice.value <= 3:
            score = await check_score(message) - 35
            await update_score(message, score)
            await sleep(3.5)
            await message.answer(f"You lose\n Score - {await check_score(message)}$")
        elif 4 <= dice.dice.value < 6:
            score = await check_score(message) + dice.dice.value * 10
            await update_score(message, score)
            await sleep(3.5)
            await message.answer(f"You <b>win!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
        else:
            score = await check_score(message) + 100
            await update_score(message, score)
            await sleep(3.5)
            await message.answer(f"<b>Strike!</b>\n Score - <b>{await check_score(message)}$</b>",
                                 parse_mode='HTML')
    else:
        await message.answer(f"For play you need 35$\n You have - {await check_score(message)}")
        await sleep(5)
        score = 50
        await update_score(message, score)
        await message.answer("Take it for play <b>+50$</b>", parse_mode='HTML')


def register_handlers_emoji(dp):
    dp.register_message_handler(send_dice, commands="dice")
    dp.register_message_handler(send_slot, commands="slot")
    dp.register_message_handler(send_dart, commands="dart")
    dp.register_message_handler(send_bowling, commands="bowling")