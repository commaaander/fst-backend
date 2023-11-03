from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .base import BaseModel
from .gendermixin import GenderMixin
from .generationmixin import GenerationMixin
from .member import Member


class SiblingRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("blood", _("blood")),
        ("half", _("half")),
        ("step", _("step")),
    )
    from_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="from_sibling_node_set")
    to_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="to_sibling_node_set")
    relationship_type = models.CharField(max_length=10, choices=RELATIONSHIP_TYPES)

    class Meta:
        unique_together = [("from_node", "to_node")]


class SpouseRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("partnership", _("partnership")),
        ("married", _("married")),
    )
    from_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="from_spouse_node_set")
    to_node = models.ForeignKey("Node", on_delete=models.CASCADE, related_name="to_spouse_node_set")
    relationship_type = models.CharField(max_length=16, choices=RELATIONSHIP_TYPES)

    class Meta:
        unique_together = [("from_node", "to_node")]


class ParentChildRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("blood", _("blood")),
        ("adopted", _("adopted")),
        ("step", _("step")),
    )
    parent = models.ForeignKey("Node", related_name="child_relations", on_delete=models.CASCADE)
    child = models.ForeignKey("Node", related_name="parent_relations", on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=50, choices=RELATIONSHIP_TYPES)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["parent", "child"], name="unique_parent_child_relation")]


class Node(Member, GenderMixin, GenerationMixin):
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
def delete_reverse_sibling_relationship(sender, instance, **kwargs):
    try:
        reverse_relationship = SiblingRelationship.objects.get(
            from_node=instance.to_node, to_node=instance.from_node, relationship_type=instance.relationship_type
        )
        reverse_relationship.delete()
    except SiblingRelationship.DoesNotExist:
        pass


@receiver(post_save, sender=SpouseRelationship)
def create_symmetrical_pouse(sender, instance, **kwargs):
    reverse_sibling, created = SpouseRelationship.objects.get_or_create(
        from_node=instance.to_node,
        to_node=instance.from_node,
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
            from_node=instance.to_node, to_node=instance.from_node, relationship_type=instance.relationship_type
        )
        reverse_relationship.delete()
    except SpouseRelationship.DoesNotExist:
        pass
