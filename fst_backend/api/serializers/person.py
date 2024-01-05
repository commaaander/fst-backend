from rest_framework import serializers

from fst_backend.api.models import Person


class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        allergy_data = validated_data.pop("allergies")
        person = Person.objects.create(**validated_data)
        person.allergies.set(allergy_data)
        return person

    def update(self, instance, validated_data):
        instance.allergies.set(validated_data.pop("allergies", []))
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
