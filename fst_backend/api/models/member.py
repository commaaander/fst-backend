from django.db import models

from .allergy import Allergy
from .base import BaseModel
from .customdate import CustomDate
from .diettypemixin import DietTypeMixin
from .gendermixin import GenderMixin
from .titlemixin import TitleMixin


class Member(BaseModel, TitleMixin, GenderMixin, DietTypeMixin):
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
    allergies = models.ManyToManyField(to=Allergy, blank=True)
    birthday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="birthday_members"
    )
    deathday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="deathday_members"
    )
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return f"{self.lastname}, {self.middlenames} {self.firstname}"
