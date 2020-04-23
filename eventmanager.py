import datetime


class Entry:
    """A single entry with all information to be imported into Google Calendar"""

    def __init__(self, summary, start, end):
        self.event = {
            'summary': summary,
            'start': start,
            'end': end
        }


class EntryList:
    """List of all entries from a single pdf"""

    def __init__(self):
        self.this_list = []

    def add_entry(self, an_entry):
        value_exists = False
        added = False
        for i in self.this_list:
            if i == an_entry:
                value_exists = True
                break
        if not value_exists:
            self.this_list.append(an_entry)
            added = True
        return added

    def remove_entry(self, an_entry):
        removed = False
        for i in self.this_list:
            if i == an_entry:
                self.this_list.remove(i)
                removed = True
                break
        return removed


def main():
    main_list = EntryList()
    test(main_list)


def test(main_list):
    start_date = datetime.datetime(2020, 4, 24, hour=10, minute=30)
    end_date = datetime.datetime(2020, 4, 24, hour=11, minute=30)
    start = {
        'dateTime': start_date.isoformat(),
        'timeZone': 'timeZone'
    }
    end = {
        'dateTime': end_date.isoformat(),
        'timeZone': 'timeZone'
    }
    event1 = Entry('Test Event 1', start, end)
    event2 = Entry('Test Event 2', start, end)
    event3 = Entry('Test Event 3', start, end)
    main_list.add_entry(event1)
    main_list.add_entry(event2)
    main_list.add_entry(event3)
    main_list.add_entry(event3)
    main_list.remove_entry(event2)
    for x in main_list.this_list:
        print(x.event['summary'])


if __name__ == "__main__":
    main()
