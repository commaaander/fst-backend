from django.contrib.auth.models import Group
from fst_backend.accounts.models import CustomUser

# from fst_backend.api.models import Member
from rest_framework import serializers

from .models import Allergy, EventMedia, Member, Tag, Event


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


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "from_day",
            "from_month",
            "from_year",
            "to_day",
            "to_month",
            "to_year",
        ]


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
