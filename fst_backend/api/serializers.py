from django.contrib.auth.models import Group
from fst_backend.accounts.models import CustomUser

# from fst_backend.api.models import Member
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Allergy, EventMedia, Member, Tag, Event, CustomDate
import re


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "url",
            "username",
            "email",
            "groups",
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "url",
            "name",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "label",
        ]


class CustomDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDate
        fields = ("day", "month", "year")


class EventSerializer(serializers.ModelSerializer):
    # from_date = CustomDateSerializer()
    # to_date = CustomDateSerializer()
    from_date = serializers.CharField(required=False, allow_blank=True, default="")
    to_date = serializers.CharField(required=False, allow_blank=True, default="")

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "from_date",
            "to_date",
        ]

    def create(self, validated_data):
        """
        Create an Event instance from validated data.
        """
        from_date_str = validated_data.pop("from_date", None)
        to_date_str = validated_data.pop("to_date", None)

        # Convert string date to CustomDate object if not empty
        if from_date_str:
            from_date = self._convert_str_to_custom_date(from_date_str)
            validated_data["from_date"] = from_date

        if to_date_str:
            to_date = self._convert_str_to_custom_date(to_date_str)
            validated_data["to_date"] = to_date

        event = Event.objects.create(**validated_data)
        return event

    def _convert_str_to_custom_date(self, date_str):
        """
        Convert a date string in format YYYY-MM-DD to CustomDate object.
        """
        year, month, day = map(int, date_str.split("-"))
        return CustomDate.objects.create(year=year, month=month, day=day)

    def validate_from_date(self, value):
        """Validate whether the from_date is in the format YYYY-MM-DD or empty."""
        return self.validate_date_format(value)

    def validate_to_date(self, value):
        """Validate whether the to_date is in the format YYYY-MM-DD or empty."""
        return self.validate_date_format(value)

    def validate_date_format(self, value):
        """Validate whether the date is in the format YYYY-MM-DD or empty."""
        if value and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
            raise serializers.ValidationError(_("The date must be in the format YYYY-MM-DD or empty."))
        return value


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


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"
