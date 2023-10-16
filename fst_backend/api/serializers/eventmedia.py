from rest_framework import serializers
from fst_backend.api.models import EventMedia


class EventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMedia
        fields = [
            "mediaUrl",
            "mimeType",
            "event",
            "from_day",
            "from_month",
            "from_year",
            "tags",
        ]
