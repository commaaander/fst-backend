from django.db import models
import uuid

from .customdate import CustomDate
from .tag import Tag


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, max_length=64)
    from_date = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="from_events"
    )
    to_date = models.ForeignKey(CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="to_events")
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
