from django.db import models
import uuid

from django.utils.translation import gettext_lazy as _


class Allergy(models.Model):
    class AllergyType(models.TextChoices):
        nuts = "nuts", _("Nüsse")
        lactose = "lactose", _("Laktose")
        sesame = "sesame", _("Sesam")
        fish = "fish", _("Fisch")
        eggs = "eggs", _("Eier")
        gluten = "gluten", _("Gluten")
        mustard = "mustard", _("Senf")
        celery = "celery", _("Sellerie")
        soy = "soy", _("Soja")
        custom = "custom", _("Sonstige")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=AllergyType.choices, default=AllergyType.custom, max_length=100)

    def __str__(self) -> str:
        return self.type
