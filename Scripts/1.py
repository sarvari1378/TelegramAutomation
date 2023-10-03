import re
from telethon.sync import TelegramClient
import asyncio

api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
channel_link = 'https://t.me/+q2xxl_QmJfxjN2Nk'  # The link to the Telegram group

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        with open('output.txt', 'w') as f:
            async for message in client.iter_messages(channel_link):
                f.write(str(message.text) + '\n')  # Save each message to the file
                f.write('-'*14 + '\n')  # Add separator after each message

# Run the async function
asyncio.run(main())
