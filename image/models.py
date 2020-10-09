import uuid

from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Image(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    base_64 = models.TextField(
        blank=True,
        null=True
    )

    extension = models.CharField(
        max_length=10,
        blank=True,
        null=False
    )

    remote_location = models.TextField(
        blank=True,
        null=True
    )

    raw_file = models.FileField(
        blank=True,
        null=True
    )

    def clean(self):
        print(self.base_64)
