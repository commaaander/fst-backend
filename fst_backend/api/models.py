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


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class EventMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
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
    tags = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self) -> str:
        return self.mediaUrl


class Allergy(models.Model):
    class AllergyType(models.TextChoices):
        nuts = "nuts", _("Nüsse")
        lactose = "lactose", _("Laktose")
        sesame = "sesame", _("Sesam")
        fish = "fish", _("Fisch")
        eggs = "eggs", _("Eier")
        gluten = "gluten", _("Gluten")
        mustard = "mustard", _("Senf")
        celery = "celery", _("Sellerie")
        soy = "soy", _("Soja")
        custom = "custom", _("Sonstige")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=AllergyType.choices, default=AllergyType.custom, max_length=100)

    def __str__(self) -> str:
        return self.type


class Member(models.Model):
    class Title(models.TextChoices):
        prof = "prof", _("Prof.")
        dr = "dr", _("Dr.")
        profDr = "profDr", _("Prof. Dr.")

    class DietType(models.TextChoices):
        vegetarian = "vegetarian", _("Vegetarisch")
        vegan = "vegan", _("Vegan")
        custom = "custom", _("Sonstige")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=True, null=True, choices=Title.choices, max_length=10)
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
    dietType = models.CharField(blank=True, null=True, choices=DietType.choices, max_length=100)
    allergies = models.ManyToManyField(to=Allergy, blank=True)
    # birthday = models.OneToOneField(CustomeDate)
    # deathday = models.OneToOneField(CustomeDate)
    placeOfBirth = models.CharField(blank=True, null=True, max_length=100)
    placeOfDeath = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return (
            f"{self.lastname}, "
            f"{self.middlenames if self.middlenames else ''} "
            f"{self.firstname if self.firstname else ''}"
        )
