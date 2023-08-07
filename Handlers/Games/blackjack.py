import random
from asyncio import sleep
from aiogram import types

from create_bot import dp, bot
from Data.Text_messages.blackjack_messages import START, BlackJack_LOSE, FINE_MESSAGE
from Keyboards.Inline_keyboards.take_card_keyboard import send_quession_keyboard
from Keyboards.Inline_keyboards.bet_keyboard import bet_keyboard_set
from Keyboards.Reply_keyboards.blackjack_keyboard import blackjack_keyboard_set
from Data_base.users_base import check_bet, check_score, update_bet, update_score


async def welcome_blackjack_message(message: types.Message):
    await message.delete()
    await message.answer(text=START, reply_markup=blackjack_keyboard_set())


player_hand = []
dealer_hand = []
deck = []
username = "none"
bet = 0
user_score = 0


async def start_blackjack_game(message: types.Message):
    global username
    global user_score
    global bet
    bet = await check_bet(message)
    user_score = await check_score(message)
    username = message.from_user.username
    if user_score >= bet > 0 and user_score > 0:
        await message.delete()
        for suit in ['♠️', '♣️', '♥️', '♦️']:
            for value in range(2, 11):
                deck.append(f'{value} {suit}')
            for value in ['J', 'Q', 'K', 'A']:
                deck.append(f'{value} {suit}')

        random.shuffle(deck)
        global player_hand
        global dealer_hand
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        await message.answer(f"""
        Dealer hand: <b>{dealer_hand[0]}</b>
You hand: <b>{"  ".join(player_hand)} </b>
       
You score - <b>{await check_score(message)}$</b>
You bet  - <b>{await check_bet(message)}$</b>

        Take a card?
        """,
                             parse_mode='HTML',
                             reply_markup=send_quession_keyboard())

        dp.register_callback_query_handler(callback, lambda call: call.data in ['yes', 'no'])
    elif user_score <= 0 <= bet:
        await message.delete()
        await message.answer("You no have money for play!\n Please wait")
        await sleep(15)
        user_score = 100
        await update_score(message, user_score)
        await message.answer("Take it for play +100$")
    elif bet > user_score > 0 or 0 >= bet:
        await message.delete()
        await message.answer("Change you bet for play.")


async def callback(call: types.CallbackQuery):
    global bet
    await bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '+50' and await check_valid_bet(call.message, 50) is True:
        await update_bet_and_send_message(call, 50)
    elif call.data == '+100' and await check_valid_bet(call.message, 100) is True:
        await update_bet_and_send_message(call, 100)
    elif call.data == '-50':
        await update_bet_and_send_message(call, -50)
    elif call.data == '-100':
        await update_bet_and_send_message(call, -100)
    elif call.data == '+250' and await check_valid_bet(call.message, 250) is True:
        await update_bet_and_send_message(call, 250)
    elif call.data == '-250':
        await update_bet_and_send_message(call, -250)
    elif call.data == '+500' and await check_valid_bet(call.message, 500) is True:
        await update_bet_and_send_message(call, 500)
    elif call.data == '-500':
        await update_bet_and_send_message(call, -500)
    elif call.data == 'all':
        await call.message.delete()
        bet = await check_score(call.message)
        await update_bet(call.message, bet)
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"You bat = {await check_bet(call.message)}",
                               reply_markup=bet_keyboard_set()
                               )

    if call.data == 'yes':
        player_hand.append(deck.pop())
        await check_winer(call.message)

    elif call.data == 'no':
        global user_score
        if bet <= 0:
            user_score -= 1000
            await update_score(call.message, user_score)
            await call.message.answer(FINE_MESSAGE, parse_mode='HTML')
        else:
            if sum_cards(player_hand) == 21:
                user_score += bet * 3
                await update_score(call.message, user_score)
                await call.message.delete()
                await bot.send_message(chat_id=call.message.chat.id,
                                       text=f"<b>@{username}</b> have <b>BlackJack!</b>\n"
                                            f"You score - {await check_score(call.message)}\n"
                                            f"You bet - {await check_bet(call.message)}",
                                       parse_mode='HTML'
                                       )
            elif sum_cards(dealer_hand) == 21:
                user_score -= bet * 3
                await update_score(call.message, user_score)
                await call.message.delete()
                await bot.send_message(chat_id=call.message.chat.id,
                                       text=f"<b>Dealer</b> have <b>BlackJack!</b>\n"
                                            f"You score - {await check_score(call.message)}\n"
                                            f"You bet - {await check_bet(call.message)}",
                                       parse_mode='HTML'
                                       )
            else:
                await check_winer(call.message)
        return call.data.lower()


async def check_winer(message: types.Message):
    global user_score
    global bet
    if sum_cards(dealer_hand) == 21:
        user_score -= bet * 3
        await bot.send_message(chat_id=message.chat.id, text=BlackJack_LOSE)
    else:
        while sum_cards(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
    await message.delete()
    player_score = sum_cards(player_hand)
    dealer_score = sum_cards(dealer_hand)
    if player_score > 21:
        user_score -= bet
        await message.answer('You lose.')
    elif dealer_score > 21:
        user_score += bet
        await message.answer('You <b>win!</b>', parse_mode='HTML')

    elif player_score > dealer_score:
        user_score += bet
        await message.answer('<b>You win!</b>', parse_mode='HTML')
    elif dealer_score > player_score:
        user_score -= bet
        await message.answer('You lose.')
    else:
        await message.answer('Draw.')
    await update_score(message, user_score)
    await message.answer(f"""
Dealer cards: <b>{"  ".join(dealer_hand)} = {dealer_score}</b>
You hand: <b>{"  ".join(player_hand)} = {player_score}</b>

You score - <b>{await check_score(message)}</b>
You bet - <b>{await check_bet(message)}</b>
""", parse_mode='HTML')


def sum_cards(hand: list) -> int:
    score: int = 0
    for card in hand:
        value = card.split()[0]
        if value.isdigit():
            score += int(value)
        elif value == 'A':
            score += 11
        else:
            score += 10
    for card in hand:
        if card.split()[0] == 'A' and score > 21:
            score -= 10
    return score


async def check_user_score(message: types.Message):
    global user_score
    user_score = await check_score(message)
    await message.delete()
    await message.answer(f"You have {await check_score(message)}$")
    return user_score


async def check_user_bet(message: types.Message):
    await message.delete()
    await message.answer(f"""You bet = <b>{await check_bet(message)}</b>
Update bet?
""", parse_mode='HTML', reply_markup=bet_keyboard_set())
    dp.register_callback_query_handler(callback,
                                       lambda call: call.data in ['+50',
                                                                  '+100',
                                                                  '-50',
                                                                  '-100',
                                                                  '+250',
                                                                  '-250',
                                                                  '+500',
                                                                  '-500',
                                                                  'all'
                                                                  ])


async def check_valid_bet(message: types.Message, upper_bet):
    if await check_bet(message) + upper_bet <= await check_score(message):
        return True
    await message.answer("You cannot bet more than your current score!")
    return False

# need comment
async def update_bet_and_send_message(call, bet_change):
    global bet
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bet += bet_change
    await update_bet(call.message, bet)
    await bot.send_message(chat_id=call.message.chat.id,
                           text=f"You bat = {await check_bet(call.message)}",
                           reply_markup=bet_keyboard_set()
                           )


def register_handlers_blackjack(dp):
    dp.register_message_handler(welcome_blackjack_message, commands=['Blackjack'])
    dp.register_message_handler(start_blackjack_game, commands=['PlayBJ'])
    dp.register_message_handler(check_user_score, commands=['score'])
    dp.register_message_handler(check_user_bet, commands=['bet'])
