from rest_framework import serializers

from fst_backend.api.models import Allergy


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"
