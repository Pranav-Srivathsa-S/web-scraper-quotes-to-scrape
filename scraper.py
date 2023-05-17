# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("http://quotes.toscrape.com/")

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the quotes on the page
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    # Extract and print the text of each quote
    text = quote.find('span', class_='text').get_text()
    print(text)

    # Extract and print the author of each quote
    author = quote.find('small', class_='author').get_text()
    print(author)

    # Extract and print the tags of each quote
    tags = quote.find('div', class_='tags').find_all('a')
    for tag in tags:
        print(tag.get_text())
    print("\n")
