if [ ! -d "$venv" ]; then
  python3 -m venv venv
  echo 'venv file is created'
else
  echo "venv exists!"
fi

sleep 1

source venv/bin/activate

pip3 install -r requirements.txt

export FLASK_APP=app.py

export FLASK_ENV=development

python -m flask run
