@ECHO off

virtualenv venv

CALL venv\Scripts\activate

pip install -r requirements.txt

set FLASK_APP=app
set FLASK_ENV=development

flask run