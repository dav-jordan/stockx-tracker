from bs4 import BeautifulSoup

import json
import requests
import sys
import time


def isUniqueObject(sale_list, object):
    sale_time = object["createdAt"]
    for sale in sale_list:
        if sale["createdAt"] == sale_time:
            return False
        # if
    # for
    return True
# def isUniqueObject

def productLoop(products, headers):
    product_dict = {}
    while True:
        for product in products:
            line = product.split(",")
            product_name = line[0]
            URL = line[1]

            # send request for url
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            #convert response to json object
            data = json.loads(str(soup))
            
            # create dictionary entry for product if it does not yet exist
            if product_name not in product_dict:
                product_dict[product_name] = []

            # loop through all sales and raise alert if given condition is met
            for sale in data["ProductActivity"]:
                if isUniqueObject(product_dict[product_name], sale):
                    print("appending")
                    product_dict[product_name].append(sale)
                # if
            # for
        # for
        
        # sleep five minutes to avoid being ip banned
        time.sleep(300)
    # while
# def productLoop

def main():
    if len(sys.argv) < 2:
        print("Please provide file with products")
        exit(0)
    # if

    # open txt file containing the api urls of products to track
    products = []
    with open(sys.argv[1]) as f:
        products = [line.rstrip() for line in f]

    # set user agent and source url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }

    productLoop(products, headers)
# def main

main()
