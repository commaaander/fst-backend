from django.core.exceptions import ValidationError
from django.db import models

from .utils import PartialDate


class PartialDateModelField(models.CharField):
    description = "A field for storing partial dates (e.g if just day and month are known)."

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self._validate_partialdate(value)

    def to_python(self, value):
        if isinstance(value, PartialDate) or value is None:
            return value
        return self._validate_partialdate(value)

    def get_prep_value(self, value):
        return str(value)

    def _validate_partialdate(self, value):
        try:
            return PartialDate(value)
        except ValueError as ve:
            raise ValidationError(ve)
