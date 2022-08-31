# DRF-Cookiecutter

[Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) project template based on [cookiecutter](https://cookiecutter.readthedocs.io/).

## What's included

* Settings via environment variables with [django-environ](https://django-environ.readthedocs.io/).
* [Celery](http://www.celeryproject.org/) configuration.
* [Django REST Framework](https://www.django-rest-framework.org/) configuration + Swagger with [drf-yasg](https://drf-yasg.readthedocs.io/).
* Typical user CRUD APIs.
* [pytest](https://docs.pytest.org/) configuration.
* Code formatting with [Black](https://black.readthedocs.io/).
* Imports sorting with [isort](https://isort.readthedocs.io/).
* [Pre-commit](https://pre-commit.com/) hook for running test & linters on each commit.
* Custom user model
* Custom documentation with [drf-yasg](https://drf-yasg.readthedocs.io/).
* Authentication setup using [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)

For more project specific details, refer the README inside the project folder.

## How to use

Create python virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install cookiecutter and packaging:

```bash
pip install cookiecutter packaging
```

Step into directory you want to create project and generate project with cookiecutter:

```bash
cd /path/to/directory
cookiecutter https://github.com/Ohuru-Tech/drf-cookiecutter
```

Answer the questions in wizard.

## Steps after project setup

Install the dependencies:

```bash
pip install -r requirements_Dev.txt
```

Copy `.env` file from example file and set your settings:

```bash
cp .env.template .env
```

Run migrations:

```bash
python manage.py migrate
```

Start building your awesome project!
