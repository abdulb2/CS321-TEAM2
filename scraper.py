from eventmanager import Entry, EntryList
from bs4 import  BeautifulSoup
from datetime import datetime

class Scraper:
    def __init__(self, html_page = None):
        self.page = html_page

    def setPage(self, html_page):
        self.page = html_page

    def scrape(self):
        entry_list = EntryList()
        soup = BeautifulSoup(open(self.page), "lxml")
        table = soup.find_all("tr")
        for table_row in table:
            single_event = []
            new_entry = None
            for item in table_row:
                if item.name == "td":
                    single_event.append(str(item.string))
            if len(single_event) != 0:
                summary, start, end = single_event
                start_date = datetime.strptime(start , "%b %d %Y")
                end_date = datetime.strptime(end , "%b %d %Y")
                new_entry = Entry(summary, start_date, end_date)
                entry_list.add_entry(new_entry)
        return entry_list