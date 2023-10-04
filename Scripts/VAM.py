import openpyxl
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

api_id = '26963557'
api_hash = '70aed19a29d2321933d9c4f652534c0f'
session = 'anon.session'

client = TelegramClient(session, api_id, api_hash)

async def get_messages(group_link, hashtag):
    VAM = []
    async with client:
        async for message in client.iter_messages(group_link):
            if message.text and hashtag in message.text:
                VAM.append(message.text.replace(hashtag, ''))
    return VAM

group_link = 'https://t.me/+q2xxl_QmJfxjN2Nk'
hashtag = 'وام'

client.start()
VAM = client.loop.run_until_complete(get_messages(group_link, hashtag))
print(VAM)


def append_to_excel(messages):
    # Open the workbook and select the sheet
    workbook = openpyxl.load_workbook('1.xlsx')
    sheet = workbook['Incomes']

    for message in messages:
        # Parse the message
        lines = message.split("\n")
        account_number = None
        amount = None
        document_number = None
        date = None
        time = None
        From = None

        for line in lines:
            if "واریز به حساب" in line:
                account_number = line.split(" ")[3]
            elif "مبلغ :" in line:
                amount = line.split(" ")[2]
            elif "مستند :" in line:
                document_number = line.split(" ")[2]
            elif "/" in line and ":" in line:
                date, time = line.split(" ")
            elif "از طرف:" in line:
                From = line.split(":")[1].strip()

        # Check if a row with the same document number, date, and time already exists
        for row in sheet.iter_rows(values_only=True):
            if row[2] == document_number and row[3] == date and row[4] == time:
                return  # Exit the function without appending if a matching row is found

        # Append the data
        if amount and account_number and document_number and date and time:
            sheet.append([amount, account_number, document_number, date, time, From])

    # Save the workbook
    workbook.save('1.xlsx')



append_to_excel(VAM)
