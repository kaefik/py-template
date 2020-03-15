"""
пример работы бота телеграмм
с кнопаками для команд

"""

import os
from dotenv import load_dotenv  # pip3 install python-dotenv
from telethon import TelegramClient, events, connection  # pip3 install Telethon
from telethon.tl.custom import Button

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
    await event.respond('Hi!')
    raise events.StopPropagation

# обработка inline кнопок
@bot.on(events.CallbackQuery)
async def handler(event):
    await event.answer('You clicked {}!'.format(event.data))

@bot.on(events.NewMessage)
async def echo(event):
    # Echo the user message.
    chat = await event.get_input_chat()
    sender = await event.get_sender()
    buttons = await event.get_buttons()
    print(sender.id)
    print(event.raw_text)
    # отправка сообщения со встроенными кнопками
    await event.respond(event.text, buttons=[[Button.inline('Left'), 
        Button.inline("MyLoc")]])

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()