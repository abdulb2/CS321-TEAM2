import requests
from bs4 import  BeautifulSoup

class Scraper:
    def __init__(self, html_page = None):
        self.page = html_page

    def setPage(self, html_page):
        self.page = html_page

    def scrape(self):
        event_list = []
        soup = BeautifulSoup(open(self.page), "lxml")
        table = soup.find_all("tr")
        for table_row in table:
            single_event = []
            for item in table_row:
                if item.name == "td":
                    single_event.append(str(item.string))
            if len(single_event) != 0:
                event_list.append(single_event)
        return event_list