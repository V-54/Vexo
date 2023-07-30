import pymysql

from Data import config

try:
    connection = pymysql.connect(
        host="localhost",
        user=config.MySQL_db_user,
        password=config.MySQL_db_password,
        database="VEXOmemory"
    )


    def check_score(message):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT score FROM users WHERE telegram_id = {message.chat.id}")
            result = cursor.fetchone()
            return result[0] if result else None


    def update_score(message, score):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE users SET score = '{score}' WHERE telegram_id = {message.chat.id}")
            connection.commit()


    def check_bet(message):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT bet FROM users WHERE telegram_id = {message.chat.id}")
            result = cursor.fetchone()
            return result[0] if result else None


    def update_bet(message, bet):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE users SET bet = '{bet}' WHERE telegram_id = {message.chat.id}")
            connection.commit()


    def add_user(full_name, name, telegram_id, language, score):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users WHERE telegram_id = %s", (telegram_id))
            result = cursor.fetchone()
            if result[0] == 0:
                cursor.execute(
                    f"INSERT INTO users (name, full_name, telegram_id, language, score) VALUE ('{full_name}', '{name}', {telegram_id}, '{language}', '{score}')")
                connection.commit()
                print("I remember this user")
            else:
                print("I already know this user")
        connection.commit()

except Exception as error:
    print("ERROR DB!")
    print(error)
