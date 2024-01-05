from rest_framework import serializers

from fst_backend.api.models import (
    Person,
    ParentChildRelationship,
    SiblingRelationship,
    SpouseRelationship,
)


class SiblingRelationshipSerializer(serializers.ModelSerializer):
    to_node = serializers.PrimaryKeyRelatedField(source="to_person", queryset=Person.objects.all())
    from_node = serializers.PrimaryKeyRelatedField(source="from_person", queryset=Person.objects.all())

    class Meta:
        model = SiblingRelationship
        fields = ["id", "url", "to_node", "from_node", "relationship_type"]


class SiblingSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="to_person", read_only=True)

    class Meta:
        model = SiblingRelationship
        fields = ("member_id", "relationship_type")


class SpouseRelationshipSerializer(serializers.ModelSerializer):
    to_node = serializers.PrimaryKeyRelatedField(source="to_person", queryset=Person.objects.all())
    from_node = serializers.PrimaryKeyRelatedField(source="from_person", queryset=Person.objects.all())

    class Meta:
        model = SpouseRelationship
        fields = ["id", "url", "to_node", "from_node", "begin_date", "end_date"]


class SpouseSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="to_person", read_only=True)

    class Meta:
        model = SpouseRelationship
        fields = ("member_id", "relationship_type")


class ParentChildRelationshipSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(source="parent", queryset=Person.objects.all())
    child_id = serializers.PrimaryKeyRelatedField(source="child", queryset=Person.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("parent_id", "child_id", "relationship_type")


class ParentRelationshipSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="parent", queryset=Person.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("member_id", "relationship_type")


class ChildRelationshipSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="child", queryset=Person.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("member_id", "relationship_type")


class NodeSerializer(serializers.ModelSerializer):
    parents = ParentRelationshipSerializer(source="parent_relations", many=True, read_only=True)
    children = ChildRelationshipSerializer(source="child_relations", many=True, read_only=True)
    siblings = SiblingSerializer(source="from_sibling_person_set", many=True, read_only=True)
    spouses = SpouseSerializer(source="from_spouse_person_set", many=True, read_only=True)

    class Meta:
        model = Person
        fields = ["lastname", "firstname", "parents", "children", "siblings", "spouses"]
