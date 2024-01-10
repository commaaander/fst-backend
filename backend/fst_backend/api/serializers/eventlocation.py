from rest_framework import serializers

from fst_backend.api.models import EventLocation


class EventLocationSerializer(serializers.ModelSerializer):
    linkUrl = serializers.URLField(source="link_url", required=None)

    class Meta:
        model = EventLocation
        fields = ["id", "url", "name", "coordinates", "caption", "linkUrl", "images"]
