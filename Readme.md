<h1 align="center">Welcome to python-django-portfolio 👋</h1>

<h3 align="center">
<a href="https://chaitanyakhairnar.io"><img alt="Live Preview" src="https://img.shields.io/badge/live%20preview-blue?link=http%3A%2F%2Fchaitanyakhairnar.io%2F"></a>
<a href="https://github.com/chaitanya-khairnar/python-django-portfolio/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/badge/license-Apache2.0-orange?link=https%3A%2F%2Fgithub.com%2Fchaitanya-khairnar%2Fpython-django-portfolio%2Fblob%2Fmain%2FLICENSE"></a>
<a href="https://codecov.io/github/chaitanya-khairnar/chaitanyakhairnar_portfolio" ><img src="https://codecov.io/github/chaitanya-khairnar/chaitanyakhairnar_portfolio/graph/badge.svg?token=ZBZN0JAGXT"/></a>
</h3>

Personal portfolio website made with Django framework in the backend, and with CSS, JS, and Bootstrap for the frontend. It is a dynamic site so that you can control the content of the site through the admin area.

## How To Use

1. Fork this repoistory and clone it to your local machine.

```bash
$ git clone https://github.com/<your-username>/python-django-portfolio.git
```

2. Go into the repository

```bash
$ cd chaitanyakhairnar-portfolio
```

3. Install dependencies usin pip

```bash
$ pip install -r requirements.txt
```

4. Make migrations
```bash
$ python manage.py migrate
```

5. Create Super User
```bash
$ python manage.py createsuperuser
```

6. Start your development server
```bash
$ python manage.py runserver
```

## Technologies Used
Python 3.10.11
Django 4.2
PostgreSQL

## Packages Used
asgiref 3.6.0
boto3 1.24.49
botocore 1.27.49
Django==4.2
django-cors-headers 3.13.0
django-storages 1.13.1
djangorestframework 3.14.0
jmespath 1.0.1
psycopg2 2.9.3
python-dateutil 2.8.2
pytz 2022.1
s3transfer 0.6.0
six 1.16.0
sqlparse 0.4.2
tzdata 2022.1
urllib3 1.26.11
python_decouple 3.8
pillow 9.5
codecov

