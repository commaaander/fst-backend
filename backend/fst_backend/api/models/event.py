from django.db import models

from fst_backend.api.fields import PartialDateField

from .base import BaseModel
from .person import Person
from .tag import Tag


class Event(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, max_length=64)
    from_date = PartialDateField()
    to_date = PartialDateField()
    organizer = models.ForeignKey(blank=True, null=True, to=Person, on_delete=models.PROTECT, related_name="events")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
