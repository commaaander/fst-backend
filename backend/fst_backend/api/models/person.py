from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from fst_backend.api.fields import PartialDateModelField

from .allergy import Allergy
from .base import BaseModel
from .diettypemixin import DietTypeMixin
from .gendermixin import GenderMixin
from .relationships import SiblingRelationship, SpouseRelationship
from .titlemixin import TitleMixin


class Person(BaseModel, TitleMixin, GenderMixin, DietTypeMixin):
    # name data
    lastname = models.CharField(max_length=100)
    middlenames = models.CharField(blank=True, null=True, max_length=100)
    firstname = models.CharField(blank=True, null=True, max_length=100)

    # birthday data
    birthday = PartialDateModelField(blank=True, null=True)
    birthname = models.CharField(blank=True, null=True, max_length=100)
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)

    # deathday data
    deathday = PartialDateModelField(blank=True, null=True)
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

    # relationship data
    parents = models.ManyToManyField(
        "self", through="ParentChildRelationship", symmetrical=False, related_name="children", blank=True
    )
    siblings = models.ManyToManyField(
        "self", through="SiblingRelationship", symmetrical=False, related_name="sibling_set", blank=True
    )
    spouses = models.ManyToManyField(
        "self", through="SpouseRelationship", symmetrical=False, related_name="spouse_set", blank=True
    )

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"


@receiver(post_save, sender=SiblingRelationship)
def create_symmetrical_sibling(sender, instance, **kwargs):
    reverse_sibling, created = SiblingRelationship.objects.get_or_create(
        from_person=instance.to_person,
        to_person=instance.from_person,
        defaults={"relationship_type": instance.relationship_type},
    )
    # If the reverse relationship exists but has a different relationship_type, update it
    if not created and reverse_sibling.relationship_type != instance.relationship_type:
        reverse_sibling.relationship_type = instance.relationship_type
        reverse_sibling.save()


@receiver(post_delete, sender=SiblingRelationship)
def delete_reverse_sibling_relationship(sender, instance, **kwargs):
    try:
        reverse_relationship = SiblingRelationship.objects.get(
            from_person=instance.to_person,
            to_person=instance.from_person,
            relationship_type=instance.relationship_type,
        )
        reverse_relationship.delete()
    except SiblingRelationship.DoesNotExist:
        pass


@receiver(post_save, sender=SpouseRelationship)
def create_symmetrical_pouse(sender, instance, **kwargs):
    reverse_sibling, created = SpouseRelationship.objects.get_or_create(
        from_person=instance.to_person,
        to_person=instance.from_person,
        defaults={"relationship_type": instance.relationship_type},
    )
    # If the reverse relationship exists but has a different relationship_type, update it
    if not created and reverse_sibling.relationship_type != instance.relationship_type:
        reverse_sibling.relationship_type = instance.relationship_type
        reverse_sibling.save()


@receiver(post_delete, sender=SpouseRelationship)
def delete_reverse_spouse_relationship(sender, instance, **kwargs):
    try:
        reverse_relationship = SpouseRelationship.objects.get(
            from_person=instance.to_person,
            to_person=instance.from_person,
            relationship_type=instance.relationship_type,
        )
        reverse_relationship.delete()
    except SpouseRelationship.DoesNotExist:
        pass
