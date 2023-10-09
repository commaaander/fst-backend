from django.db import models
from django.utils.translation import gettext_lazy as _


class GenerationMixin(models.Model):
    GENERATION_CHOICES = (
        ("not_specified", _("----")),
        ("yellow", _("yellow")),
        ("orange", _("orange")),
        ("green", _("green")),
        ("blue", _("blue")),
        ("red", _("Female")),
        ("violet", _("Diverse")),
    )

    generation = models.CharField(max_length=15, choices=GENERATION_CHOICES)

    class Meta:
        abstract = True
