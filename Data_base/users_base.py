import aiomesql
from loguru import logger

from Data import config

logger.add('Log/users.log', format='{time}  {level}  {message}', level='DEBUG')
logger.add('Log/ERROR.log', format='{time}  {level}  {message}', level='ERROR')

try:
    async def connect_to_database():
        return await aiomysql.connect(
            host="localhost",
            user=config.MySQL_db_user,
            password=config.MySQL_db_password,
            db="VEXOmemory"
        )


    async def check_score(message):
        async with connect_to_database() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(f"SELECT score FROM users WHERE telegram_id = {message.chat.id}")
                result = await cursor.fetchone()
                return result[0] if result else None


    async def update_score(message, score):
        async with connect_to_database() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(f"UPDATE users SET score = '{score}' WHERE telegram_id = {message.chat.id}")
                await connection.commit()


    async def check_bet(message):
        async with connect_to_database() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(f"SELECT bet FROM users WHERE telegram_id = {message.chat.id}")
                result = await cursor.fetchone()
                return result[0] if result else None


    async def update_bet(message, bet):
        async with connect_to_database() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(f"UPDATE users SET bet = '{bet}' WHERE telegram_id = {message.chat.id}")
                await connection.commit()


    async def add_user(full_name, name, telegram_id, language, score):
        async with connect_to_database() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT COUNT(*) FROM users WHERE telegram_id = %s", (telegram_id))
                result = await cursor.fetchone()
                if result[0] == 0:
                    await cursor.execute(
                        'INSERT INTO users (name, full_name, telegram_id, language, score) VALUES (%s, %s, %s, %s, %s)',
                        (name, full_name, telegram_id, language, score)
                    )
                    await connection.commit()
                    print("I remember this user")
                else:
                    print("I already know this user")
            await connection.commit()


except Exception as error:
    logger.error(error)
