from __future__ import absolute_import

import os

from configurations.importer import install
from django.conf import settings

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

install(check_options=True)
app = Celery("{{ cookiecutter.project_slug }}")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
