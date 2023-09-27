import asyncio
import requests
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

# Fetch chat IDs from the 'Users.txt' file hosted on GitHub
def fetch_chat_ids_from_github(filename):
    chat_ids = []
    url = 'https://raw.githubusercontent.com/yourusername/yourrepository/main/' + filename
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        for line in lines:
            if line.strip():
                username, number, chat_id = line.strip().split(', ')
                chat_id = int(chat_id)
                chat_ids.append((username, chat_id))
    return chat_ids

if __name__ == "__main__":
    # Specify the filename in your GitHub repository
    github_filename = 'Users.txt'

    # Fetch chat IDs from the file hosted on GitHub
    chat_ids = fetch_chat_ids_from_github(github_filename)

    # Run the asynchronous function within an event loop for each chat ID
    loop = asyncio.get_event_loop()
    for username, chat_id in chat_ids:
        loop.run_until_complete(send_message(username, chat_id))
