from rest_framework import serializers

from fst_backend.api.models import CustomDate


class CustomDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDate
        fields = ("day", "month", "year")
