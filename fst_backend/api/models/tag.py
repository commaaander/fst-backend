from django.db import models
import uuid


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.label
