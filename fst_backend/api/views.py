from django.contrib.auth.models import Group
from fst_backend.accounts.models import CustomUser
from .models import Event, EventMedia, Tag, Member, Allergy, CustomDate
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    CustomUserSerializer,
    GroupSerializer,
    EventSerializer,
    TagSerializer,
    EventMediaSerializer,
    MemberSerializer,
    AllergySerializer,
    CustomDateSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomDateViewSet(viewsets.ModelViewSet):
    queryset = CustomDate.objects.all()
    serializer_class = CustomDateSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventMediaViewSet(viewsets.ModelViewSet):
    queryset = EventMedia.objects.all()
    serializer_class = EventMediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [permissions.IsAuthenticated]
