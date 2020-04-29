import editor
import eventmanager
import googleAPI
import scraper
import upload
import secrets
from flask import Flask , request

app = Flask(__name__)
app.secret_key = secrets.token_hex(64)

UPLOAD_FOLDER = ""
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.add_url_rule('/insert_event' , view_func=googleAPI.insert_events)
app.add_url_rule('/calendar' , view_func=googleAPI.calendar)
app.add_url_rule('/welcome' , view_func=googleAPI.welcome)
app.add_url_rule('/' , view_func=upload.upload_file , methods=['POST' , 'GET'])
app.add_url_rule('/uploads' , view_func=upload.uploaded_file , methods=['POST' , 'GET'])
app.add_url_rule('/editor' , view_func=editor.main , methods=['POST' , 'GET'])
app.add_url_rule('/editor/add_entry' , view_func=editor.add_entry, methods=['GET' , 'POST'])


