import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from progimage.settings import broker_url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progimage.settings')

app = Celery('progimage', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')