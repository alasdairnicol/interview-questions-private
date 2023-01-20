Installation
============

This project uses Django 3.2, so requires Python >=3.6 and <3.11.

You can create a virtual environment as follows:

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run project
===========

```
source venv/bin/activate
cd ths
# run migrations to create a local sqlite database
./manage.py migrate
./manage.py runserver
````

Run test suite
==============

```
source venv/bin/activate
cd ths
./manage.py test
````