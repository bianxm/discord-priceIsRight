from bs4 import BeautifulSoup
import requests

class AmazonInfo():
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'Accept-Language':'en-US, en;q=0.5'})
    
    def __init__(self, url):
        self.soup = BeautifulSoup(requests.get(url, headers = self.HEADERS).content, 'lxml')
    
    def get_title(self):
        try:
            return self.soup.find("span", attrs={"id":"productTitle"}).string.strip()
        except AttributeError:
            return "Error getting title"

    def get_price(self):
        try:
            return self.soup.find("span", attrs={"class":"a-offscreen"}).string
        except AttributeError:
            return "Error getting price"

    def get_img(self):
        try:
            return self.soup.find("img", attrs={"id":"landingImage"})['data-old-hires']
        except AttributeError:
            return "Error getting image"

    def get_features(self):
        try:
            return [i.string for i in list(self.soup.find('div',attrs={'id':'feature-bullets'}).select('span',attrs={'class':'a-list-item'}))]
        except AttributeError:
            return "Error getting features"