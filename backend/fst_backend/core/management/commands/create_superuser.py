import os

from django.core.management.base import BaseCommand

from fst_backend.accounts.models import CustomUser


class Command(BaseCommand):
    help = "Creates the initial superuser"

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "passwort123")

            CustomUser.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {username=} and {email=} created!"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists."))
