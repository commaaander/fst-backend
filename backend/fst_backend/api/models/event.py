from django.db import models

from fst_backend.api.fields import PartialDateModelField

from .base import BaseModel
from .person import Person
from .tag import Tag


class Event(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    from_date = PartialDateModelField()
    to_date = PartialDateModelField()
    registration_until = models.DateTimeField(blank=True, null=True)
    organizer = models.ManyToManyField(Person, blank=True, related_name="events")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
