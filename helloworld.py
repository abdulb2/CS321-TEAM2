from __future__ import print_function
import flask
from flask import Flask
from flask import request, render_template, redirect, session , url_for
import secrets
import datetime
import pickle
import os.path
from urllib.parse import urlparse
import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from requests_oauthlib import OAuth2Session

app = Flask(__name__)
app.secret_key = secrets.token_hex(64)


@app.route('/')
def hello_world():
    return render_template('hello_world.html', name = 'Ashwin')


@app.route('/calendar', methods=['get', 'post'])
def calendar():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_id.json', 
    scopes=[
        'https://www.googleapis.com/auth/calendar'
    ])

    flow.redirect_uri = 'http://127.0.0.1:5000/welcome'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    return redirect(authorization_url)


@app.route('/welcome', methods=['get', 'post'])
def welcome():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_id.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        )
    flow.redirect_uri = url_for('welcome', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    
    credentials = flow.credentials
    session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return redirect(url_for('insert_events'))

@app.route('/insert_event' , methods=['get' , 'post'])
def insert_events():
    if('credentials' not in session):
        return redirect(url_for('calendar'))
    credentials = google.oauth2.credentials.Credentials(**session['credentials'])
    service = build('calendar' , 'v3' , credentials=credentials)
    calendar = service.calendars().get(calendarId='primary').execute()
    start_date = datetime.datetime(2020 , 4 , 24 , hour = 10 , minute = 30)  
    end_date = datetime.datetime(2020 , 4 , 24 , hour = 11 , minute = 30)
    event = {
        'summary': 'Test event insertion',
        'start':{
            'dateTime' : start_date.isoformat(),
            'timeZone' : calendar['timeZone']
        },
        'end':{
            'dateTime' : end_date.isoformat(),
            'timeZone' : calendar['timeZone']
        }
    }
    event_sent = service.events().insert(calendarId = 'primary' , body=event).execute()
    
    session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    return 'Event has been added'