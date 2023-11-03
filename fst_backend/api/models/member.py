from django.db import models

from .allergy import Allergy
from .base import BaseModel
from .customdate import CustomDate
from .diettypemixin import DietTypeMixin
from .gendermixin import GenderMixin
from .titlemixin import TitleMixin


class Member(BaseModel, TitleMixin, GenderMixin, DietTypeMixin):
    # name data
    lastname = models.CharField(max_length=100)
    middlenames = models.CharField(blank=True, null=True, max_length=100)
    firstname = models.CharField(blank=True, null=True, max_length=100)

    # birthday data
    birthday = models.ForeignKey(
        CustomDate,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="birthday_members",
    )
    birthname = models.CharField(blank=True, null=True, max_length=100)
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)

    # deathday data
    deathday = models.ForeignKey(
        CustomDate,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="deathday_members",
    )
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)

    # adress
    address = models.CharField(blank=True, null=True, max_length=100)
    zip = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=100)
    country = models.CharField(blank=True, null=True, max_length=100)

    # contact
    email = models.EmailField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)

    # health data
    allergies = models.ManyToManyField(to=Allergy, blank=True)

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"
