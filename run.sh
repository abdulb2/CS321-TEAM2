
if [! -e '$venv']
then
    virtualenv -p `which python3` venv
    echo 'venv file is created'
fi
echo 'venv exists!'

sleep 1

source venv/bin/activate

pip3 install -r requirements.txt

export FLASK_APP=app.py

export FLASK_ENV=development

python -m flask run
