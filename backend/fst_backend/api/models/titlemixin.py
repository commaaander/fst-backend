from django.db import models
from django.utils.translation import gettext_lazy as _


class TitleMixin(models.Model):
    TITLE__CHOICES = (
        ("not_specified", _("----")),
        ("prof", _("Prof.")),
        ("dr", _("Dr.")),
        ("profDr", _("Prof. Dr.")),
    )

    title = models.CharField(max_length=15, choices=TITLE__CHOICES, default="not_specified")

    class Meta:
        abstract = True
