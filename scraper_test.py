from eventmanager import EntryList, Entry
from scraper import Scraper

scraper = Scraper()
scraper.setPage("./course_table.html")

entry_list = scraper.scrape()

for entry in entry_list.this_list:
    print(entry.get_event())

