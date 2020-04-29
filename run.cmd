@ECHO off
IF NOT EXIST 'venv'(
	virtualenv venv
)
ELSE(
	echo "file exists!"
)

venv\Scripts\activate.bat

pip install -r requirements.txt

set FLASK_APP=app
set FLASK_ENV=development

flask run
