import base64
import io
import os

from celery import Celery, shared_task

from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.core.files.base import ContentFile

from image.models import Image
from progimage.settings import broker_url
from PIL import Image as Im

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progimage.settings')

app = Celery('progimage', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')


@app.task(bind=True)
def convert(self, image):
    image = Image.objects.get(id=image)
    print(image)
    print(image.base_64)
    print(base64.b64decode(image.base_64))
    im = Im.open(io.BytesIO(base64.b64decode(image.base_64)))
    with io.BytesIO() as f:
        im.save(f, format='JPEG')
        f_data = ContentFile(f.getvalue())
        image.jpeg.save(f"{image.id}.jpeg", f_data)

        im.save(f, format='PNG')
        f_data = ContentFile(f.getvalue())
        image.png.save(f"{image.id}.png", f_data)




