from telethon.sync import TelegramClient, events

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
    async for message in client.iter_messages(entity, reverse=True):
        if message.text or message.media:
            break

    # Forward the message to the channel
    forwarded_message = f"{message.text}\n\nChannel ID: {channel_username}"
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
