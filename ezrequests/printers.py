import requests
from bs4 import BeautifulSoup

url = 'https://www.zackplauche.com'


def h1_printer(url):
    """Get the h1 tag from any url and print it!"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.find('h1')
    print(h1_tag.text)


def h2_printer(url):
    """Print all h2 tag texts in a list format."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        print(h2.text)
