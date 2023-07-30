from aiogram import executor

from create_bot import dp
from Handlers.Client import register_handlers_client
from Handlers.Games.blackjack import register_handlers_blackjack
from Handlers.Games.emoji_games import register_handlers_emoji
from Handlers.Games.dices import register_handlers_dice


def main():
    register_handlers_client(dp)
    register_handlers_blackjack(dp)
    register_handlers_emoji(dp)
    register_handlers_dice(dp)

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    print("Vexo starting...")
    main()
