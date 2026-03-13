## Create virtual environment
```bash
python -m venv venv
```
## Activate virtual environment
```bash
venv/Scripts/activate.ps1
```
## Install dependencies
```bash
pip install -r requirements.txt
```

## Create database
```bash
CREATE DATABASE market_db;
```
## Migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Start Application
```bash
python manage.py runserver
```