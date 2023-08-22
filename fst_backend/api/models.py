from django.db import models
import uuid

from django.utils.translation import gettext_lazy as _

from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.label


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, max_length=64)
    from_day = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    from_month = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(13)],
    )
    from_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1000), MaxValueValidator(10000)],
    )
    to_day = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    to_month = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(13)],
    )
    to_year = (
        models.PositiveIntegerField(
            blank=True, null=True, validators=[MinValueValidator(1000), MaxValueValidator(10000)]
        ),
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title


class EventMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaUrl = models.CharField(max_length=1024)
    mimeType = models.CharField(max_length=64)
    event = models.ForeignKey(blank=True, null=True, to=Event, on_delete=models.CASCADE)
    from_day = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    from_month = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(13)],
    )
    from_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1000), MaxValueValidator(10000)],
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.mediaUrl


class Member(models.Model):
    class Title(models.TextChoices):
        prof = "prof", _("Prof.")
        dr = "dr", _("Dr.")
        profDr = "profDr", _("Prof. Dr.")
        none = "none", ""

    class DietType(models.TextChoices):
        vegetarian = "vegetarian", _("Vegetarisch")
        vegan = "vegan", _("Vegan")
        custom = "custom", _("Sonstige")
        none = "none", ""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(choices=Title.choices, default=Title.none, max_length=10)
    firstname = models.CharField(blank=True, null=True, max_length=100)
    lastname = models.CharField(max_length=100)
    middlenames = models.CharField(blank=True, null=True, max_length=100)
    birthname = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(blank=True, null=True, max_length=100)
    zip = models.CharField(blank=True, null=True, max_length=10)
    city = models.CharField(blank=True, null=True, max_length=100)
    country = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    dietType = models.CharField(choices=DietType.choices, default=DietType.none, max_length=10)
    # birthday = models.OneToOneField(CustomeDate)
    # deathday = models.OneToOneField(CustomeDate)
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return f"{self.lastname}, {self.middlenames if self.middlenames else ''} {self.firstname}"


# class Allergies(models.Model):
#     class Allergy(models.TextChoices):
#         nuts = ("nuts", _("Nüsse"))
#         lactose = ("lactose", _("Laktose"))
#         sesame = ("sesame", _("Sesam"))
#         fish = ("fish", _("Fisch"))
#         eggs = ("eggs", _("Eier"))
#         gluten = ("gluten", _("Gluten"))
#         mustard = ("mustard", _("Senf"))
#         celery = ("celery", _("Sellerie"))
#         soy = ("soy", _("Soja"))
#         custom = ("custom", _("Sonstige"))

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     type = models.CharField(choices=Allergy, default="custom")
#     member = models.ForeignKey(to=Member, on_delete=models.CASCADE, related_name="allergies")
