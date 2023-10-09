from django.db import models
import uuid

from django.utils.translation import gettext_lazy as _

from .allergy import Allergy
from .customdate import CustomDate


class Member(models.Model):
    class Title(models.TextChoices):
        prof = "prof", _("Prof.")
        dr = "dr", _("Dr.")
        profDr = "profDr", _("Prof. Dr.")

    class DietType(models.TextChoices):
        vegetarian = "vegetarian", _("Vegetarisch")
        vegan = "vegan", _("Vegan")
        custom = "custom", _("Sonstige")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=True, null=True, choices=Title.choices, max_length=10)
    firstname = models.CharField(blank=True, null=True, max_length=100)
    lastname = models.CharField(max_length=100)
    middlenames = models.CharField(blank=True, null=True, max_length=100)
    birthname = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(blank=True, null=True, max_length=100)
    zip = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=100)
    country = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    dietType = models.CharField(blank=True, null=True, choices=DietType.choices, max_length=100)
    allergies = models.ManyToManyField(to=Allergy, blank=True)
    # birthday = models.OneToOneField(CustomeDate)
    birthday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="birthday_members"
    )
    deathday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="deathday_members"
    )
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return (
            f"{self.lastname}, "
            f"{self.middlenames if self.middlenames else ''} "
            f"{self.firstname if self.firstname else ''}"
        )
