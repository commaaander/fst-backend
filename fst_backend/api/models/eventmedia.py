from django.db import models
from PIL import Image

from .base import BaseModel
from .customdate import CustomDate
from .event import Event
from .tag import Tag


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class EventMedia(BaseModel):
    mediaUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    mimeType = models.CharField(max_length=64)
    event = models.ForeignKey(blank=True, null=True, to=Event, on_delete=models.CASCADE)
    from_date = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.SET_NULL, related_name="eventmedia_froms"
    )
    tags = models.ManyToManyField(to=Tag, blank=True)
    thumbnailUrl = models.ImageField(upload_to="thumbnails/", blank=True, null=True, editable=False)

    def get_thumbnailUrl(self):
        if self.thumbnailUrl:
            return self.thumbnailUrl.url

        if self.mediaUrl:
            image = Image.open(self.mediaUrl.path)
            thumbnail_size = (100, 100)
            image.thumbnail(thumbnail_size)
            thumbnail_path = "thumbnails/{}_thumbnail.jpg".format(self.id)
            image.save(thumbnail_path)
            self.thumbnailUrl.name = thumbnail_path
            self.save()
            return self.thumbnailUrl.url

        return None

    def __str__(self) -> str:
        return self.id
