from telethon.sync import TelegramClient, events
from datetime import datetime, timedelta
import pytz
import asyncio

# Your API credentials
api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'

# Session file name
session_file = 'anon.session'

# Group link and channel username
group_link = 'https://t.me/+q2xxl_QmJfxjN2Nk'
channel_username = '@sajed_sugests'

async def main():
    # Create a Telethon client using the session file
    client = TelegramClient(session_file, api_id, api_hash)

    # Connect and log in
    await client.start()

    # Find the group using the group link
    try:
        entity = await client.get_entity(group_link)
    except ValueError:
        print("Invalid group link.")
        return

    # Find the oldest message in the group
    message = None
    async for msg in client.iter_messages(entity, reverse=True):
        if msg.text or msg.media:
            message = msg
            break

    # Get current time in Iran
    tz_iran = pytz.timezone('Asia/Tehran')
    now_iran = datetime.now(tz_iran)
    
    # Calculate how long to wait until the next half-hour mark
    minutes_to_wait = 30 - now_iran.minute % 30
    if minutes_to_wait < 30:
        await asyncio.sleep(minutes_to_wait * 60)  # Convert minutes to seconds

    # If a message exists, forward it to the channel and delete it from the group
    if message is not None:
        forwarded_message = f"{message.text}\n\n🆔: {channel_username}"
        if message.media:
            await client.send_message(channel_username, forwarded_message, file=message.media)
        else:
            await client.send_message(channel_username, forwarded_message)

        # Delete the message from the group
        await client.delete_messages(entity, message)

    # Disconnect
    await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
