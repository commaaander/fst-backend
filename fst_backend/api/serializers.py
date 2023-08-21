from django.contrib.auth.models import Group
from fst_backend.accounts.models import CustomUser

from rest_framework import serializers


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "url", "name"]
