from datetime import datetime
import eventmanager
import scraper
import googleAPI

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)


def main():
    if request.method == 'POST':
        val = int(request.form['index'])
        session['entry_list'].pop(val)
        return render_template('editor.html', entry_list=session['entry_list'])
    if 'entry_list' not in session.keys():
        print('came in here')
        filename = session['filename']
        scrap = scraper.Scraper(filename)
        scrap_list = scrap.scrape()
        entry_list = scrap_list.get_list()
        dict_list = []
        for i in entry_list:
            dict_list.append(i.get_event())
        session['entry_list'] = dict_list
    return render_template('editor.html', entry_list=session['entry_list'])


def add_entry():
    if request.method == "POST":
        summary = request.form['summary']
        start_date = request.form['start_date']
        print(start_date)
        end_date = request.form['due_date']
        start = datetime.strptime(start_date.strip(), "%Y-%m-%d")
        end = datetime.strptime(end_date ,"%Y-%m-%d")
        entry = eventmanager.Entry(summary, start, end)
        session['entry_list'].append(entry.get_event())
        session.modified = True
        return redirect(url_for('main'))
    return render_template('add_entry.html')



if __name__ == "__main__":
    main()
