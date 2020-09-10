import requests
from bs4 import BeautifulSoup

# open txt file containing the api urls of products to track
urls = open("products.txt")

# set user agent and source url
headers = {
    'User-Agent': 'YOUR USER AGENT'
    }
URL = 'https://stockx.com/api/products/e90e1888-61f0-4681-8379-a4706e491235/activity?state=480&currency=USD&limit=10&page=1&sort=createdAt&order=DESC&country=US'

# send request for url
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
