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
        from_date_str = validated_data.pop("from_date", None)
        to_date_str = validated_data.pop("to_date", None)

        if from_date_str:
            from_date = self._convert_str_to_custom_date(from_date_str)
            validated_data["from_date"] = from_date

        if to_date_str:
            to_date = self._convert_str_to_custom_date(to_date_str)
            validated_data["to_date"] = to_date

        event = Event.objects.create(**validated_data)
        return event

    def _convert_str_to_custom_date(self, date_str):
        year, month, day = map(int, date_str.split("-"))
        return CustomDate.objects.create(year=year, month=month, day=day)

    def validate_from_date(self, value):
        return self.validate_date_format(value)

    def validate_to_date(self, value):
        return self.validate_date_format(value)

    def validate_date_format(self, value):
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

    birthday = serializers.CharField(required=False, allow_blank=True, default="")
    deathday = serializers.CharField(required=False, allow_blank=True, default="")

    def create(self, validated_data):
        birthday_str = validated_data.pop("birthday", None)
        deathday_str = validated_data.pop("deathday", None)

        if birthday_str:
            from_date = self._convert_str_to_custom_date(birthday_str)
            validated_data["birthday"] = from_date

        if deathday_str:
            to_date = self._convert_str_to_custom_date(deathday_str)
            validated_data["deathday"] = to_date

        event = Member.objects.create(**validated_data)
        return event

    def _convert_str_to_custom_date(self, date_str):
        year, month, day = map(int, date_str.split("-"))
        return CustomDate.objects.create(year=year, month=month, day=day)

    def validate_birthday(self, value):
        return self.validate_date_format(value)

    def validate_deathday(self, value):
        return self.validate_date_format(value)

    def validate_date_format(self, value):
        if value and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
            raise serializers.ValidationError(_("The date must be in the format YYYY-MM-DD or empty."))
        return value


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"
