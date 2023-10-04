from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import re
from datetime import datetime
import pytz

api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
session = 'anon.session'
channel_usernames = ['@V2rayCollectorDonate']  # Add your channels here

client = TelegramClient(session, api_id, api_hash)

async def main():
    async with client:
        all_links = []
        for channel_username in channel_usernames:
            channel_entity = await client.get_entity(channel_username)
            offset_id = 0
            vless_trojan_links = []
            while len(vless_trojan_links) < 20:
                posts = await client(GetHistoryRequest(
                    peer=channel_entity,
                    limit=100,  # Get more messages per request
                    offset_date=None,
                    offset_id=offset_id,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0))

                for message in posts.messages:
                    links = re.findall('vless://[^\s]+|trojan://[^\s]+', message.message)
                    vless_trojan_links.extend(links)
                    all_links.extend(links)
                    if len(vless_trojan_links) >= 20:
                        break

                if not posts.messages:
                    break  # No more messages left

                offset_id = posts.messages[-1].id

            with open(f'{channel_username}.txt', 'w') as f:
                for i, link in enumerate(vless_trojan_links[:20]):  # Only write the first 20 links
                    # Get current time in Iran/Tehran
                    tehran_tz = pytz.timezone('Asia/Tehran')
                    tehran_time = datetime.now(tehran_tz)
                    hour_minute = tehran_time.strftime('%H:%M')

                    # Replace all characters after '#' with '|Channel_Username|$Hour|X|'
                    modified_link = re.sub('#.*', f'#|{hour_minute}|{i+1}|', link)
                    f.write(f'{modified_link}\n')

        with open('merged.txt', 'w') as f:
            for i, link in enumerate(all_links[:20]):  # Only write the first 20 links
                # Get current time in Iran/Tehran
                tehran_tz = pytz.timezone('Asia/Tehran')
                tehran_time = datetime.now(tehran_tz)
                hour_minute = tehran_time.strftime('%H:%M')

                # Replace all characters after '#' with '|Channel_Username|$Hour|X|'
                modified_link = re.sub('#.*', f'#|{hour_minute}|{i+1}|', link)
                f.write(f'{modified_link}\n')

client.loop.run_until_complete(main())
