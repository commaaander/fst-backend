from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import BaseModel


class EventLocation(BaseModel):
    name = models.CharField(max_length=64)
    coordinates = models.TextField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    images = ArrayField(models.TextField(blank=True, null=True), default=list, blank=True)

    def __str__(self) -> str:
        return self.name
