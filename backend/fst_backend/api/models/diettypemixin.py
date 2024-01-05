from django.db import models
from django.utils.translation import gettext_lazy as _


class DietTypeMixin(models.Model):
    DIET_TYPE__CHOICES = (
        ("not_specified", _("----")),
        ("vegetarian", _("Vegetarian")),
        ("vegan", _("Vegan")),
        ("others", _("Other")),
    )

    dietType = models.CharField(max_length=15, choices=DIET_TYPE__CHOICES, default="not_specified")

    class Meta:
        abstract = True
