from .member import Member
from .base import BaseModel

from django.db import models

from .customdate import CustomDate
from .tag import Tag


class Event(BaseModel):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, max_length=64)
    from_date = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="from_events"
    )
    to_date = models.ForeignKey(CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="to_events")
    organizer = models.ForeignKey(blank=True, null=True, to=Member, on_delete=models.PROTECT, related_name="events")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
