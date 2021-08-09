from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


class Scrapper:

    def __init__(self):
        self.page_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"
        self.product_name = []
        self.product_rating = []
        self.product_price = []

    def information_scrapper(self):
        for page_number in range(1, 12):
            uClient = uReq(self.page_url.format(page_number))
            page_soup = soup(uClient.read(), "html.parser")
            uClient.close()
            containers = page_soup.findAll("div", {"class": "_3pLy-c row"})
            for container in containers:
                try:
                    if float('{}'.format(container.find("div", {"class": "_3LWZlK"}).get_text())) > 4.5:
                        self.product_name.append('{}'.format(container.find("div", {"class": "_4rR01T"}).get_text()))
                        self.product_rating.append('{}'.format(container.find("div", {"class": "_3LWZlK"}).get_text()))
                        self.product_price.append(
                            '{}'.format(container.find("div", {"class": "_30jeq3 _1_WHN1"}).get_text()))
                except AttributeError:
                    pass
        return self.product_name, self.product_rating, self.product_price
