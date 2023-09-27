import asyncio
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5978875502:AAFHqLOAQahaMklBX7n9K3GUk7YCKIm2sF0'

async def send_message(username, chat_id):
    # Initialize the bot
    bot = Bot(token=bot_token)

    # Define message text based on the specified conditions
    if 5 <= chat_id <= 10:
        message_text = 'Hello, @{}! This is a message for users with chat ID between 5 and 10.'.format(username)
    elif 2 <= chat_id < 5:
        message_text = 'Hello, @{}! This is a message for users with chat ID between 2 and 5.'.format(username)
    elif chat_id < 2:
        message_text = 'Hello, @{}! This is a message for users with chat ID less than 2.'.format(username)
    else:
        message_text = 'Hello, @{}! This is a generic message.'.format(username)

    # Send the message to the recipient
    await bot.send_message(chat_id=chat_id, text=message_text)

# Read chat IDs from the 'Users.txt' file
def read_chat_ids_from_file(filename):
    chat_ids = []
    with open(filename, 'r') as file:
        for line in file:
            username, number, chat_id = line.strip().split(', ')
            chat_id = int(chat_id)
            chat_ids.append((username, chat_id))
    return chat_ids

if __name__ == "__main__":
    # File path to 'Users.txt' in your GitHub repository
    file_path = 'https://raw.githubusercontent.com/sarvari1378/TelegramAutomation/main/Users.txt'

    # Read chat IDs from the file
    chat_ids = read_chat_ids_from_file(file_path)

    # Run the asynchronous function within an event loop for each chat ID
    loop = asyncio.get_event_loop()
    for username, chat_id in chat_ids:
        loop.run_until_complete(send_message(username, chat_id))
