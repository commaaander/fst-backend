from django.db import models
from django.utils.translation import gettext_lazy as _

from fst_backend.api.fields import PartialDateModelField

from .base import BaseModel


class SiblingRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("blood", _("blood")),
        ("half", _("half")),
        ("step", _("step")),
    )
    from_person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="from_sibling_person_set")
    to_person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="to_sibling_person_set")
    relationship_type = models.CharField(max_length=10, choices=RELATIONSHIP_TYPES)

    class Meta:
        unique_together = [("from_person", "to_person")]

    def __str__(self):
        return _("{}  <->  {} ").format(self.from_person, self.to_person)


class SpouseRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("partnership", _("partnership")),
        ("married", _("married")),
    )
    from_person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="from_spouse_person_set")
    to_person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="to_spouse_person_set")
    relationship_type = models.CharField(max_length=16, choices=RELATIONSHIP_TYPES)
    begin_date = PartialDateModelField()
    end_date = PartialDateModelField()

    class Meta:
        unique_together = [("from_person", "to_person")]

    def __str__(self):
        return _("{}  <->  {} ").format(self.from_person, self.to_person)


class ParentChildRelationship(BaseModel):
    RELATIONSHIP_TYPES = (
        ("blood", _("blood")),
        ("adopted", _("adopted")),
        ("step", _("step")),
    )
    parent = models.ForeignKey("Person", related_name="child_relations", on_delete=models.CASCADE)
    child = models.ForeignKey("Person", related_name="parent_relations", on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=50, choices=RELATIONSHIP_TYPES)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["parent", "child"], name="unique_parent_child_relation")]

    def __str__(self):
        return _("{} ->  {}").format(self.parent, self.child)
