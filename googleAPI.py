from __future__ import print_function
from flask import request, render_template, redirect, session, url_for
from pytz import timezone
import datetime
import os.path
import google.oauth2.credentials
import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from requests_oauthlib import OAuth2Session
import eventmanager

def hello_world():
    return render_template('hello_world.html', name='Ashwin')

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


def insert_events():
    if ('credentials' not in session.keys()):
        return redirect(url_for('calendar'))
    credentials = google.oauth2.credentials.Credentials(**session['credentials'])
    service = build('calendar', 'v3', credentials=credentials)
    eastern = timezone('US/eastern')
    for items in session['entry_list']:
        event = {
            'summary': items['summary'],
            'start':{
                'dateTime': eastern.localize(items['start']).isoformat(),
            },
            'end':{
                'dateTime' : eastern.localize(items['end']).isoformat(),
            }
        }
        service.events().insert(calendarId='primary', body=event).execute()
    session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    return render_template('hello_world.html')
