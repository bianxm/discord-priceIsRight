from bs4 import BeautifulSoup
import requests

class AmazonInfo():
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'Accept-Language':'en-US, en;q=0.5'})
    
    def __init__(self, url):
        soup = BeautifulSoup(requests.get(url, headers = self.HEADERS).content, 'lxml')
        
        try:
            self.title = soup.find("span", attrs={"id":"productTitle"}).string.strip()
        except AttributeError:
            self.title = "Error getting title"

        try:
            self.price = soup.find("span", attrs={"class":"a-offscreen"}).string
        except AttributeError:
            self.price = "Error getting price"

        try:
            self.imgUrl = soup.find("img", attrs={"id":"landingImage"})['data-old-hires']
        except AttributeError:
            self.imgUrl = "Error getting image"

        try:
            self.featureList = [i.string.strip() for i in list(soup.find('div',attrs={'id':'feature-bullets'}).select('span',attrs={'class':'a-list-item'}))]
        except AttributeError:
            self.featureList = "Error getting features"