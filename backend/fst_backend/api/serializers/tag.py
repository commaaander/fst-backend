from rest_framework import serializers

from fst_backend.api.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "label",
        ]
