import discord
from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5'})

URL = 'https://a.co/d/izrlUwo'

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, 'lxml')

try:
    title = soup.find("span", attrs={"id":"productTitle"}).string.strip()
except AttributeError:
    print("Error getting title")

try:
    price = soup.find("span", attrs={"class":"a-offscreen"}).string
except AttributeError:
    print("Error getting price")

try:
    imgUrl = soup.find("img", attrs={"id":"landingImage"})['data-old-hires']
except AttributeError:
    print("Error getting image")

try:
    featureList = list(soup.find('div',attrs={'id':'feature-bullets'}).select('span',attrs={'class':'a-list-item'}))
except AttributeError:
    print("Error getting features")