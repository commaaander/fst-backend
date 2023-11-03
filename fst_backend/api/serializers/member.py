from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from fst_backend.api.models import CustomDate, Member, Node


class MemberSerializer(serializers.ModelSerializer):
    birthday = serializers.RegexField(
        regex=r"^\d{4}-\d{2}-\d{2}$",
        required=False,
        allow_blank=True,
        default="",
        help_text=_("Format: YYYY-MM-DD"),
    )
    deathday = serializers.RegexField(
        regex=r"^\d{4}-\d{2}-\d{2}$",
        required=False,
        allow_blank=True,
        default="",
        help_text=_("Format: YYYY-MM-DD"),
    )

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
        instance.allergies.set(validated_data.pop("allergies", []))

        for attribute in ["birthday", "deathday"]:
            date_str = validated_data.pop(attribute)
            if date_str:
                year, month, day = map(int, date_str.split("-"))
                date = getattr(instance, attribute)
                if date:
                    setattr(date, "year", year)
                    setattr(date, "month", month)
                    setattr(date, "day", day)
                    try:
                        date.full_clean()
                        date.save()
                    except ValidationError as ve:
                        raise serializers.ValidationError({attribute: ve.messages})

                else:
                    setattr(instance, attribute, CustomDate.objects.create(year=year, month=month, day=day))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    def convert_str_to_custom_date(self, date_str):
        if date_str:
            year, month, day = map(int, date_str.split("-"))
            return CustomDate.objects.create(year=year, month=month, day=day)
        return None
