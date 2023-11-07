import requests
from aiogram import Bot, types
from aiogram.dispatcher import dispatcher
import logging
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot_token = '6911644031:AAGWT-c1LTUd22AeV1Nob-YERQTo0nuOYhk'

# Initialize the bot and dispatcher
bot = Bot(token=bot_token)

async def on_start():
    # Replace 'RECIPIENT_CHAT_ID' with the chat ID where you want to send the file
    chat_id = '462288021'
    file_url = 'https://dls.music-fa.com/tagdl/1402/Shoara%20-%20Daste%20Khali%20(320).mp3'

    try:
        # Download the file from the given URL
        response = requests.get(file_url)
        file_name = file_url.split("/")[-1]

        # Send the file to the specified chat
        with open(file_name, 'wb') as file:
            file.write(response.content)
        await bot.send_document(chat_id, types.InputFile(file_name), caption=f"File: {file_name}")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_start())
    loop.close()
