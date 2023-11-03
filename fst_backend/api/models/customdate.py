from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class CustomDate(BaseModel):
    day = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(31)])
    month = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(12)])
    year = models.PositiveIntegerField(blank=True, null=True)

    def clean(self):
        if self.day and self.month:
            try:
                date(year=self.year or 2000, month=self.month, day=self.day)
            except ValueError:
                raise ValidationError(_("Invalid date: Month {:02d} has no day {:02d}").format(self.month, self.day))

    def __str__(self):
        return "{:04d}-{:02d}-{:02d}".format(self.year or 0, self.month or 0, self.day or 0)
