from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from fst_backend.api.models import Event, CustomDate
import re


class EventSerializer(serializers.ModelSerializer):
    from_date = serializers.CharField(required=False, allow_blank=True, default="")
    to_date = serializers.CharField(required=False, allow_blank=True, default="")

    class Meta:
        model = Event
        fields = ["id", "url", "title", "description", "from_date", "to_date", "organizer"]

    def create(self, validated_data):
        from_date_str = validated_data.pop("from_date", "")
        to_date_str = validated_data.pop("to_date", "")

        validated_data["from_date"] = self.convert_str_to_custom_date(from_date_str)
        validated_data["to_date"] = self.convert_str_to_custom_date(to_date_str)

        event = Event.objects.create(**validated_data)
        return event

    def update(self, instance, validated_data):
        from_date_str = validated_data.pop("from_date", "")
        to_date_str = validated_data.pop("to_date", "")

        instance.from_date = self.convert_str_to_custom_date(from_date_str)
        instance.to_date = self.convert_str_to_custom_date(to_date_str)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def convert_str_to_custom_date(self, date_str):
        if date_str:
            year, month, day = map(int, date_str.split("-"))
            return CustomDate.objects.create(year=year, month=month, day=day)
        return None

    def validate_from_date(self, value):
        return self.validate_date_format(value)

    def validate_to_date(self, value):
        return self.validate_date_format(value)

    def validate_date_format(self, value):
        if value and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
            raise serializers.ValidationError(_("The date must be in the format YYYY-MM-DD or empty."))
        return value
