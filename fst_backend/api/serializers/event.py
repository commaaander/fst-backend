from rest_framework import serializers

from fst_backend.api.models import Event


class EventSerializer(serializers.ModelSerializer):
    from_date = serializers.CharField(required=False, allow_blank=True, default="")
    to_date = serializers.CharField(required=False, allow_blank=True, default="")

    class Meta:
        model = Event
        fields = ["id", "url", "title", "description", "from_date", "to_date", "organizer"]
