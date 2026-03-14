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

## Create database(from PostgreSQL terminal)
#### PostgreSQL should be installed and /bin/ should be added in Environmental Variables(Windows).
```bash
psql -U postgres

CREATE DATABASE market_db;
\q
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

## API Endpoints Implemented

### 1. POST `/api/candles/` 
### 2. GET `/api/candles/`
### 3. GET `/api/candles/{id}`
### 4. PUT `/api/candles/{id}`
### 5. DELETE `/api/candles/{id}`