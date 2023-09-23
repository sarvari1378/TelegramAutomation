import requests
from bs4 import BeautifulSoup
import os

# Get the URL from the environment variable
url = os.getenv("URL")

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract all the text within the HTML
        plain_text = soup.get_text()

        # Print the extracted plain text
        print(plain_text)

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
