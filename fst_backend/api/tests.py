from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Member, Allergy
from .serializers import MemberSerializer


class MemberAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Testdaten
        self.member_data = {
            "lastname": "Doe",
            "firstname": "John",
            "middlenames": "Middle",
            "gender": "Male",
            "title": "Mr.",
        }
        self.member = Member.objects.create(**self.member_data)

        self.allergy = Allergy.objects.create(type="sesame")
        self.allergy_data = [self.allergy.id]

        self.url = reverse("member-list")

    def test_create_member(self):
        response = self.client.post(self.url, self.member_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 2)

    def test_read_member(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_member(self):
        updated_data = {
            "lastname": "Smith",
            "middlenames": "Updated Middle",
        }
        response = self.client.put(reverse("member-detail", args=[self.member.id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.member.refresh_from_db()
        self.assertEqual(self.member.lastname, "Smith")
        self.assertEqual(self.member.middlenames, "Updated Middle")

    def test_delete_member(self):
        response = self.client.delete(reverse("member-detail", args=[self.member.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Member.objects.count(), 0)


class MemberSerializerTest(TestCase):
    def test_serializer_create(self):
        allergy = Allergy.objects.create(type="sesame")
        data = {
            "lastname": "Smith",
            "firstname": "Alice",
            "middlenames": "Middle",
            "gender": "Female",
            "title": "Ms.",
            "birthday": "1990-01-01",
            "deathday": "2022-03-15",
            "allergies": [allergy.id],
        }
        serializer = MemberSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        member = serializer.save()
        self.assertEqual(member.lastname, "Smith")
        self.assertEqual(member.allergies.count(), 1)

    def test_serializer_update(self):
        member = Member.objects.create(lastname="Doe", firstname="John")
        allergy1 = Allergy.objects.create(type="sesame")
        allergy2 = Allergy.objects.create(type="mustard")
        data = {
            "lastname": "Smith",
            "middlenames": "Updated Middle",
            "allergies": [allergy1.id, allergy2.id],
        }
        serializer = MemberSerializer(instance=member, data=data)
        self.assertTrue(serializer.is_valid())
        updated_member = serializer.save()
        self.assertEqual(updated_member.lastname, "Smith")
        self.assertEqual(updated_member.middlenames, "Updated Middle")
        self.assertEqual(updated_member.allergies.count(), 2)
