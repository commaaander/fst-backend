from rest_framework import serializers
from fst_backend.api.models import EventMedia


class EventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMedia
        fields = ["id", "url", "mediaUrl", "thumbnailUrl", "mimeType", "event", "from_date", "tags"]
