from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from fst_backend.api.models import Member


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.OneToOneField(null=True, blank=True, to=Member, on_delete=models.SET_NULL)
