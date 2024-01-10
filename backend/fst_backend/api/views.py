from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from fst_backend.accounts.models import CustomUser
from fst_backend.accounts.serializers import CustomUserSerializer, GroupSerializer

from .models import (
    Allergy,
    Event,
    EventMedia,
    ParentChildRelationship,
    Person,
    SiblingRelationship,
    SpouseRelationship,
    Tag,
)
from .serializers import (
    AllergySerializer,
    EventMediaSerializer,
    EventSerializer,
    MemberSerializer,
    NodeSerializer,
    ParentChildRelationshipSerializer,
    PersonsSerializer,
    SiblingRelationshipSerializer,
    SpouseRelationshipSerializer,
    TagSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("id")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class EventMediaViewSet(viewsets.ModelViewSet):
    queryset = EventMedia.objects.all().order_by("id")
    serializer_class = EventMediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("lastname", "firstname")
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all().order_by("type")
    serializer_class = AllergySerializer
    permission_classes = [permissions.IsAuthenticated]


class SiblingRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SiblingRelationship.objects.all()
    serializer_class = SiblingRelationshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpouseRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SpouseRelationship.objects.all()
    serializer_class = SpouseRelationshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParentChildRelationshipSerializerViewSet(viewsets.ModelViewSet):
    queryset = ParentChildRelationship.objects.all()
    serializer_class = ParentChildRelationshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class NodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all().order_by("lastname", "firstname")
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by("lastname", "firstname")
    serializer_class = PersonsSerializer
    permission_classes = [permissions.IsAuthenticated]
