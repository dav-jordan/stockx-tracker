import requests
from bs4 import BeautifulSoup

# set user agent and source url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
URL = 'http://stockx.com/air-jordan-1-retro-high-satin-snake-chicago-w'

# send request for url
page = requests.get(URL, headers=headers)

# print page html
print(page.text)
