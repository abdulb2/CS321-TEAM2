

source venv/bin/activate

pip3 install -r requirements.txt

export FLASK_APP=helloworld.py

export FLASK_ENV=development

python -m flask run