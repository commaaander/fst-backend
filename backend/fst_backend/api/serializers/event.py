from rest_framework import serializers

from fst_backend.api.models import Event

from fst_backend.api.fields import PartialDateSerializerField


class EventSerializer(serializers.ModelSerializer):
    to = PartialDateSerializerField(required=False, allow_blank=True, default="", source="to_date")
    vars()["from"] = PartialDateSerializerField(required=False, allow_blank=True, default="", source="from_date")
    registrationUntil = serializers.DateTimeField(source="registration_until")

    class Meta:
        model = Event
        fields = [
            "url",
            "id",
            "title",
            "description",
            "signature",
            "organizer",
            "from",
            "to",
            "registrationUntil",
        ]
