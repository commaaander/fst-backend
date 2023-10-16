from rest_framework import serializers
from fst_backend.api.models import (
    Node,
    SiblingRelationship,
    SpouseRelationship,
    ParentChildRelationship,
)


class SiblingRelationshipSerializer(serializers.ModelSerializer):
    to_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())
    from_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())

    class Meta:
        model = SiblingRelationship
        fields = "__all__"


class SiblingSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="to_node", read_only=True)

    class Meta:
        model = SiblingRelationship
        fields = ("member_id", "relationship_type")


class SpouseRelationshipSerializer(serializers.ModelSerializer):
    to_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())
    from_node = serializers.PrimaryKeyRelatedField(queryset=Node.objects.all())

    class Meta:
        model = SpouseRelationship
        fields = "__all__"


class SpouseSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="to_node", read_only=True)

    class Meta:
        model = SpouseRelationship
        fields = ("member_id", "relationship_type")


class ParentChildRelationshipSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(source="parent", queryset=Node.objects.all())
    child_id = serializers.PrimaryKeyRelatedField(source="child", queryset=Node.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("parent_id", "child_id", "relationship_type")


class ParentRelationshipSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="parent", queryset=Node.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("member_id", "relationship_type")


class ChildRelationshipSerializer(serializers.ModelSerializer):
    member_id = serializers.PrimaryKeyRelatedField(source="child", queryset=Node.objects.all())

    class Meta:
        model = ParentChildRelationship
        fields = ("member_id", "relationship_type")


class NodeSerializer(serializers.ModelSerializer):
    parents = ParentRelationshipSerializer(source="parent_relations", many=True, read_only=True)
    children = ChildRelationshipSerializer(source="child_relations", many=True, read_only=True)
    siblings = SiblingSerializer(source="from_sibling_node_set", many=True, read_only=True)
    spouses = SpouseSerializer(source="from_spouse_node_set", many=True, read_only=True)

    class Meta:
        model = Node
        fields = "__all__"
