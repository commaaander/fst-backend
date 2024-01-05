from django.db import models

from .base import BaseModel


class Tag(BaseModel):
    label = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.label
