import requests
from bs4 import  BeautifulSoup

class Scraper:
    def __init__(self, html_page = None):
        self.page = html_page

    def setPage(self, html_page):
        self.page = html_page

    def scrape(self):
        retVal = [[]]
        soup = BeautifulSoup(open(self.page), "lxml")
        #print(soup.prettify())
        #print(soup)
        links = soup.find_all("tr")
        singleEvent = []
        for row in links:
            print("row:")
            for item in row:
                print(item)
                #print(type(item))