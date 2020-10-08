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

    remote_location = models.TextField(
        blank=True,
        null=True
    )
