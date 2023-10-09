from django.db import models
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .customdate import CustomDate
from .gendermixin import GenderMixin
from .generationmixin import GenerationMixin
from django.utils.translation import gettext_lazy as _


class SiblingRelationship(models.Model):
    RELATIONSHIP_TYPES = (
        ("blood", _("blood")),
        ("half", _("half")),
        ("step", _("step")),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="from_node_set")
    to_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="to_node_set")
    relationship_type = models.CharField(max_length=10, choices=RELATIONSHIP_TYPES)

    class Meta:
        unique_together = [("from_node", "to_node")]


class Node(GenderMixin, GenerationMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lastname = models.CharField(blank=True, null=True, max_length=100)
    firstname = models.CharField(blank=True, null=True, max_length=100)
    middlenames = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    birthday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="birthday_nodes"
    )
    deathday = models.ForeignKey(
        CustomDate, blank=True, null=True, on_delete=models.CASCADE, related_name="deathday_nodes"
    )
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)
    placeholder = models.BooleanField(blank=True, null=True)
    parents = models.ManyToManyField("self", symmetrical=False, related_name="children", blank=True)
    siblings = models.ManyToManyField(
        "self", through="SiblingRelationship", symmetrical=False, related_name="sibling_set", blank=True
    )
    spouses = models.ManyToManyField("self", symmetrical=True, blank=True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}".strip()


@receiver(post_save, sender=SiblingRelationship)
def create_symmetrical_sibling(sender, instance, **kwargs):
    reverse_sibling, created = SiblingRelationship.objects.get_or_create(
        from_node=instance.to_node,
        to_node=instance.from_node,
        defaults={"relationship_type": instance.relationship_type},
    )
    # If the reverse relationship exists but has a different relationship_type, update it
    if not created and reverse_sibling.relationship_type != instance.relationship_type:
        reverse_sibling.relationship_type = instance.relationship_type
        reverse_sibling.save()


@receiver(post_delete, sender=SiblingRelationship)
def delete_reverse_relationship(sender, instance, **kwargs):
    try:
        reverse_relationship = SiblingRelationship.objects.get(
            from_node=instance.to_node, to_node=instance.from_node, relationship_type=instance.relationship_type
        )
        reverse_relationship.delete()
    except SiblingRelationship.DoesNotExist:
        pass
