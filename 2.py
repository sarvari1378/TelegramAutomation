import os
import re
import requests
from telethon.sync import TelegramClient
import asyncio

api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
channel_link = 'https://t.me/BOTISMINE'  # The link to the Telegram group
session_url = 'https://github.com/sarvari1378/TelegramAutomation/raw/main/anon.session'  # The URL of the session file

# Download the session file
response = requests.get(session_url)
session_data = response.content

async def main():
    client = TelegramClient(StringIO(session_data), api_id, api_hash)
    await client.start()
    async with client:
        with open('output.txt', 'w') as f:
            async for message in client.iter_messages(channel_link):
                f.write(str(message.text) + '\n')  # Save each message to the file
                f.write('-'*14 + '\n')  # Add separator after each message

# Run the async function
asyncio.run(main())
