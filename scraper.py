import requests
from bs4 import BeautifulSoup

# set user agent and source url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
URL = 'https://stockx.com/search/sneakers?s=Jordan%201%20Retro%20High%20Satin%20Snake%20Chicago'

# send request for url
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
