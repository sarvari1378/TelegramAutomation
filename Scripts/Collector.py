from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import re

api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
session = 'anon.session'
channel_username = '@V2rayCollectorDonate'

client = TelegramClient(session, api_id, api_hash)

async def main():
    async with client:
        channel_entity = await client.get_entity(channel_username)
        posts = await client(GetHistoryRequest(
            peer=channel_entity,
            limit=20,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))

        vless_links = []
        for message in posts.messages:
            links = re.findall('vless://[^\s]+', message.message)
            vless_links.extend(links)

        with open(f'{channel_username}.txt', 'w') as f:
            for link in vless_links:
                f.write(f'{link}\n')

client.loop.run_until_complete(main())
