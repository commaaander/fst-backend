from rest_framework import serializers

from fst_backend.api.models import Person
from .allergy import AllergySerializer


class MemberSerializer(serializers.ModelSerializer):
    allergies = AllergySerializer(read_only=False, many=True)

    class Meta:
        model = Person
        fields = [
            "url",
            "id",
            "lastname",
            "firstname",
            "middlenames",
            "gender",
            "title",
            "birthday",
            "placeOfBirth",
            "birthname",
            "deathday",
            "placeOfDeath",
            "address",
            "zip",
            "city",
            "country",
            "email",
            "phone",
            "allergies",
            "dietType",
        ]
