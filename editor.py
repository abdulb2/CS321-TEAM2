import datetime
import eventmanager

from flask import Flask, render_template, request

app = Flask(__name__)

entry_list = eventmanager.EntryList()


# editor is the interface between the eventmanager and the user


@app.route('/editor', methods=['GET', 'POST'])
def main():
    return render_template('editor.html', entry_list)


@app.route('editor/add_entry', methods=['GET', 'POST'])
def add_entry():
    summary = request.form('summary')
    start_date = request.form('start_date')
    end_date = request.form('due_date')
    start = datetime.datetime(start_date)
    end = datetime.datetime(end_date)
    entry = entrymanager.Entry(summary, start, end)
    entry_list.add_entry(entry)
    return render_template('add_entry.html')


def delete_entry():
    render_template('delete_entry.html')


def edit_entry():
    render_template('edit_entry.html')


if __name__ == "__main__":
    main()
