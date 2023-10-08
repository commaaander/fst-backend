from django.db import models
import uuid

from .tag import Tag
from .event import Event
from django.core.validators import MinValueValidator, MaxValueValidator


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class EventMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    mimeType = models.CharField(max_length=64)
    event = models.ForeignKey(blank=True, null=True, to=Event, on_delete=models.CASCADE)
    from_day = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    from_month = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(13)],
    )
    from_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1000), MaxValueValidator(10000)],
    )
    tags = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self) -> str:
        return self.mediaUrl
