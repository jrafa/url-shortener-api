url-shortener-api
=============

### Introduction:
Url shortener API.

### Requirements:
* Python 3.10
* Django 5.0
* DRF 3.15

### Installation:
* Clone repo:
```bash
git clone https://github.com/jrafa/url-shortener-api.git
```
* Install requirements and activate virtual environment:
```bash
poetry install
poetry shell
```

* Run migration:
```bash
python manage.py migrate --fake
```
* Run locally by PyCharm IDE or in terminal:
```bash
python manage.py runserver
```
* Run tests:
```bash
pytest -v
```