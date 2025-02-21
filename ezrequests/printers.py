import requests
from bs4 import BeautifulSoup

url = 'https://www.zackplauche.com'


def h1_printer(url):
    """Get the h1 tag from any url and print it!"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.find('h1')
    print(h1_tag.text)
