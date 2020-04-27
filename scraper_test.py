from eventmanager import EntryList, Entry
from scraper import Scraper

scraper = Scraper()
scraper.setPage("./course_table.html")
assignments = scraper.scrape()

entry_list = EntryList()

for assignment in assignments:
    summary, start, end = assignment
    new_entry = Entry(summary, start, end)
    entry_list.add_entry(new_entry)

for entry in entry_list.this_list:
    print(entry.event)