from telethon import TelegramClient, events
import os

API_ID = '26963557'
API_HASH = '70aed19a29d2321933d9c4f652534c0f'
CHANNEL_NAME = '@Tak_Mesra'

client = TelegramClient('session', API_ID, API_HASH)

async def main():
    messages = []
    async for message in client.iter_messages(CHANNEL_NAME):
        messages.append(message.text)

    if not os.path.exists('Posts'):
        os.makedirs('Posts')

    for i, message in enumerate(messages):
        with open(f'Posts/{i+1}.txt', 'w') as f:
            f.write(message)

with client:
    client.loop.run_until_complete(main())
