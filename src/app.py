__author__ = 'lw'

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?colour=Red")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "now-price", "itemprop": "price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print("Buy the chair")
    print("The current price is {}.".format(price))
else:
    print("Don't buy the chair")
# <span class="now-price" itemprop="price"> £115.00 </span>
