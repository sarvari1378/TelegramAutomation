import asyncio
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5978875502:AAFHqLOAQahaMklBX7n9K3GUk7YCKIm2sF0'

async def send_message():
    # Initialize the bot
    bot = Bot(token=bot_token)

    # Replace 'YOUR_MESSAGE' with the message you want to send
    message_text = 'Hello, @ssarvari1378! This is a test message from my Python script.'

    # Replace '@ssarvari1378' with the username of the recipient
    recipient_username = '462288021'

    # Send the message to the recipient
    await bot.send_message(chat_id=recipient_username, text=message_text)

# Run the asynchronous function within an event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message())
