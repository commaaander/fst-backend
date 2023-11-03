from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from fst_backend.api.models import Member, CustomDate, Node
import re


class MemberSerializer(serializers.ModelSerializer):
    birthday = serializers.CharField(required=False, allow_blank=True, default="", help_text=_("Format: YYYY-MM-DD"))
    deathday = serializers.CharField(required=False, allow_blank=True, default="", help_text=_("Format: YYYY-MM-DD"))

    class Meta:
        model = Member
        fields = [
            "url",
            "id",
            "lastname",
            "firstname",
            "middlenames",
            "gender",
            "title",
            "birthday",
            "deathday",
            "dietType",
            "birthname",
            "address",
            "zip",
            "city",
            "country",
            "email",
            "phone",
            "placeOfBirth",
            "placeOfDeath",
            "allergies",
        ]

    def create(self, validated_data):
        allergies_data = validated_data.pop("allergies", [])
        validated_data["birthday"] = self.convert_str_to_custom_date(validated_data.get("birthday"))
        validated_data["deathday"] = self.convert_str_to_custom_date(validated_data.get("deathday"))

        member = Member.objects.create(**validated_data)
        node = Node(member_ptr=member)
        node.save_base(raw=True)

        member.allergies.set(allergies_data)

        return member

    def update(self, instance, validated_data):
        allergies_data = validated_data.pop("allergies", [])
        instance.allergies.set(allergies_data)

        instance.birthday = self.convert_str_to_custom_date(validated_data.get("birthday"))
        instance.deathday = self.convert_str_to_custom_date(validated_data.get("deathday"))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    def convert_str_to_custom_date(self, date_str):
        if date_str:
            year, month, day = map(int, date_str.split("-"))
            return CustomDate.objects.create(year=year, month=month, day=day)
        return None

    def validate_birthday(self, value):
        return self.validate_date_format(value)

    def validate_deathday(self, value):
        return self.validate_date_format(value)

    def validate_date_format(self, value):
        if value and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
            raise serializers.ValidationError(_("The date must be in the format YYYY-MM-DD or empty."))
        return value
