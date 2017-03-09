__author__ = 'lw'

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?colour=Red")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "now-price", "itemprop": "price"})
print(element.text)

# <span class="now-price" itemprop="price"> £115.00 </span>
