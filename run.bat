@ECHO off

virtualenv venv

CALL venv\Scripts\activate

pip install -r requirements.txt

set FLASK_APP=helloworld
set FLASK_ENV=development

flask run