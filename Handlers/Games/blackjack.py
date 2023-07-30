import random
from time import sleep
from aiogram import types

from create_bot import dp, bot
from Data.Text_messages.blackjack_messages import START, BlackJack_LOSE
from Keyboards.Inline_keyboards.take_card_keyboard import send_quession_keyboard
from Keyboards.Inline_keyboards.bet_keyboard import bet_keyboard_set
from Keyboards.Reply_keyboards.blackjack_keyboard import blackjack_keyboard_set
from Data_base.users_base import check_bet, check_score, update_bet, update_score


async def start_game(message: types.Message):
    await message.delete()
    await message.answer(text=START, reply_markup=blackjack_keyboard_set())


player_hand = []
dealer_hand = []
deck = []
username = "none"
bet = 0
user_score = 0

async def play_game(message: types.Message):

    global username
    global user_score
    global bet
    bet = check_bet(message)
    user_score = check_score(message)
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
        You hand: <b>{", ".join(player_hand)}</b>
        Dealer hand: <b>{dealer_hand[0]}</b>
       
    You score - <b>{check_score(message)}$</b>
    You bet  - <b>{check_bet(message)}$</b>

        Take a card?
        """,
                             parse_mode='HTML',
                             reply_markup=send_quession_keyboard())

        dp.register_callback_query_handler(callback, lambda call: call.data in ['yes', 'no'])
    elif user_score <= 0:
        await message.delete()
        await message.answer("You no have money for play!\n Please wait")
        sleep(15)
        user_score = 100
        update_score(message, user_score)
        await message.answer("Take it for play +100$")
    elif bet > user_score > 0 or 0 >= bet:
        await message.delete()
        await message.answer("Change you bet for play.")


async def callback(call: types.CallbackQuery):
    global bet
    await bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '+50':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bet += 50
        update_bet(call.message, bet)
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"You bat = {check_bet(call.message)}",
                               reply_markup=bet_keyboard_set()
                               )
    elif call.data == '+100':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bet += 100
        update_bet(call.message, bet)
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"You bat = {check_bet(call.message)}",
                               reply_markup=bet_keyboard_set()
                               )
    elif call.data == '-50':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bet -= 50
        update_bet(call.message, bet)
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"You bat = {check_bet(call.message)}",
                               reply_markup=bet_keyboard_set()
                               )
    elif call.data == '-100':
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bet -= 100
        update_bet(call.message, bet)
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"You bat = {check_bet(call.message)}",
                               reply_markup=bet_keyboard_set()
                               )

    if call.data == 'yes':
        player_hand.append(deck.pop())
        await check_winer(call.message)

    elif call.data == 'no':
        global user_score
        if sum_cards(player_hand) == 21:
            user_score += bet*3
            update_score(call.message, user_score)
            await bot.send_message(chat_id=call.message.chat.id,
                                   text=f"<b>@{username}</b> have <b>BlackJack!</b>",
                                   parse_mode='HTML'
                                   )
        elif sum_cards(dealer_hand) == 21:
            user_score -= bet * 3
            update_score(call.message, user_score)
            await bot.send_message(chat_id=call.message.chat.id,
                                   text=BlackJack_LOSE
                                   )
        else:
            await check_winer(call.message)
    return call.data.lower()


async def check_winer(message: types.Message):

    global user_score
    global bet

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
    update_score(message, user_score)
    await message.answer(f"""
You hand: <b>{", ".join(player_hand)}</b>
Dealer cards: <b>{", ".join(dealer_hand)}'</b>

You score - <b>{check_score(message)}</b>
You bet - <b>{check_bet(message)}</b>
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
    await message.delete()
    await message.answer(f"You have {check_score(message)}$")


async def check_user_bet(message: types.Message):
    await message.delete()
    await message.answer(f"""You bet = <b>{check_bet(message)}</b>
Update bet?
""", parse_mode='HTML', reply_markup=bet_keyboard_set())
    dp.register_callback_query_handler(callback,
                                       lambda call: call.data in ['+50', '+100', '-50', '-100'])


def register_handlers_blackjack(dp):
    dp.register_message_handler(start_game, commands=['Blackjack'])
    dp.register_message_handler(play_game, commands=['PlayBJ'])
    dp.register_message_handler(check_user_score, commands=['score'])
    dp.register_message_handler(check_user_bet, commands=['bet'])