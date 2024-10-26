# scraper.py


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

# Example usage
#url = 'https://en.wikipedia.org/wiki/Neurosteroid'
#text = scrape_website(url)
#print(text)
