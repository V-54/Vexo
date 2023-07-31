## Vexo

### Description

That is a telegram bot for playing minigames and blackjack, also you can roll dices and much more
<!--
TODO нужно полностью обновить и актуализировать разделы устновки и функционала бота
можно добавить гифки и улучшить оформление файла в целом
-->

## INSTALLATION

To install the necessary packages, run the following command:

```
pip install -r requirements.txt
```

Then, create a new bot in Telegram and obtain the API token. Add the token and your admin chat ID to the `config.py` file located in the `Data/` directory.
*(you need to create a config.py file)*

```
# you bot token from @BotFather
TOKEN = 'you bot token'

# that bot version using MySQL db for working
MySQL_db_name='VEXOmemory'
MySQL_db_user='root'
MySQL_db_password='you_password'

# you ID
admin_chat_id = 123456789
```

To start the bot, run the following command:

```
python3 main.py
```
**if you see a message in the console**
> Vexo starting

So the bot listens for incoming messages and responds accordingly.

### Features

- **/start - starting bot**

- **/help - send commands list**

- **/dices - list of dice**

- **/games - games list**

- **/picture - list of pictures**

- **/link - message with links**

- **/sticker - send a sticker**

- **/settings - edit to settings menu**

- **/about - about developer**
