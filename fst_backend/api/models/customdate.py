from django.db import models
import uuid

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
from datetime import datetime


class CustomDate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.PositiveIntegerField(blank=True, null=True)
    month = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)

    def clean(self):
        # Check if day, month, and year are present and form a valid date.
        if self.day and self.month:
            try:
                # If the year isn't set, use a leap year to allow for February 29th.
                datetime(year=self.year or 2000, month=self.month, day=self.day)
            except ValueError:
                raise ValidationError(
                    _("Invalid date: {year:04d}-{month:02d}-{day:02d}").format(
                        year=self.year or 0, month=self.month or 0, day=self.day or 0
                    )
                )

    def __str__(self):
        return "{year:04d}-{month:02d}-{day:02d}".format(year=self.year or 0, month=self.month or 0, day=self.day or 0)
