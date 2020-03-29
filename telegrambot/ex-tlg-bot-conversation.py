"""
пример работы бота телеграмм

с conversation (диалога)
чтобы войти в диалог нужно ввести команду /AddUser

"""

import os
from dotenv import load_dotenv  # pip3 install python-dotenv
from telethon import TelegramClient, events, connection  # pip3 install Telethon

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
print((dotenv_path))
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
app_api_id = os.getenv("TLG_APP_API_ID")
app_api_hash = os.getenv("TLG_APP_API_HASH")
app_name = os.getenv("TLG_APP_NAME")
bot_token = os.getenv("I_BOT_TOKEN")
client = os.getenv("TLG_CLIENT")
proxy_server = os.getenv("TLG_PROXY_SERVER")
proxy_port = int(os.getenv("TLG_PROXY_PORT"))
proxy_key = os.getenv("TLG_PROXY_KEY")

proxy = (proxy_server, proxy_port, proxy_key)
bot = TelegramClient(app_name, app_api_id, app_api_hash,
                            connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
                            proxy=proxy)
bot.start(bot_token=bot_token)

# client = [] # клиент

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Привет!\nЧтобы войти в диалог нужно ввести команду /AddUser')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/AddUser'))
async def echo(event):    
    # диалог с запросом информации нужной для работы команды /AddUser
    await event.respond("Выполняется команда /AddUSer")
    chat_id = event.chat_id
    async with bot.conversation(chat_id) as conv:
        #response = conv.wait_event(events.NewMessage(incoming=True))
        await conv.send_message("Привет! Введите номер id пользователя"\
            "который нужно добавить для доступа к боту:")
        id_new_user = await conv.get_response()
        id_new_user = id_new_user.message        
        # id пользователя должен быть числом
        while not any(x.isdigit() for x in id_new_user):
            await conv.send_message("ID нового пользователя - это число. Попробуйте еще раз.")
            id_new_user = await conv.get_response()
            id_new_user = id_new_user.message
        # print("id_new_user ", id_new_user)       
        await conv.send_message(f"Добавили нового пользователя с ID: {id_new_user}")

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()