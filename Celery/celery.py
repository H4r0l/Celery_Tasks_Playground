import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Celery.settings")

app = Celery("Celery")
app.config_from_object("django.conf:settings", namespace="Celery")

app.autodiscover_tasks()