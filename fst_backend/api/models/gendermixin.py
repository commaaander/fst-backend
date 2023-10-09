from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderMixin(models.Model):
    GENDER_CHOICES = (
        ("not_specified", _("----")),
        ("male", _("Male")),
        ("female", _("Female")),
        ("diverse", _("Diverse")),
    )

    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    class Meta:
        abstract = True
