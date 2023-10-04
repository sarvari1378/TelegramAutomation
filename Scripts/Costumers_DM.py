from telethon.sync import TelegramClient
import csv
import os
import requests  # Import the requests library

# Replace these with your own values
api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
Session_file = 'anon.session'

client = TelegramClient(Session_file, api_id, api_hash)
client.start()

# Replace 'your_url_here' with the actual URL containing the user data in CSV format
url = 'https://raw.githubusercontent.com/sarvari1378/SingBOX/main/Users.txt'  # The URL you want to get the content from
response = requests.get(url)  # Send a GET request to the URL

# Save the content of the URL to 'Users.txt'
with open('Users.txt', 'w') as f:
    f.write(response.text)

user_data_file = 'Users.txt'
users = []

with open(user_data_file, 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        data = line.split(',')
        if len(data) == 3:
            name, date, username = data
            users.append((name, float(date), username))

for user in users:
    name, date, username = user
    if date == 5:
        message = "سلام عرض ادب و احترام. بنده درخدمتم اگر مشکلی در سیستم هست بفرمایید"
    elif date == 2:
        message = "سلام عرض ادب و احترام اشتراک شما رو به پایان است آیا قصد تمدید دارید؟"
    else:
        continue

    try:
        client.send_message(username, message)
        print(f"Message sent to {username}")
    except Exception as e:
        print(f"Could not send message to {username}. Error: {e}")

client.disconnect()
