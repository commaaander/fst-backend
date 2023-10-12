from django.core.management.base import BaseCommand
from fst_backend.api.models import Allergy


class Command(BaseCommand):
    help = "Initialize database with some base content (e.g. allergy types)"

    def handle(self, *args, **options):
        self.stdout.write("Init allergy database.")
        for allergy_type in Allergy.AllergyType:
            if not Allergy.objects.filter(type=allergy_type.value).exists():
                Allergy.objects.create(type=allergy_type.value)
                self.stdout.write(self.style.SUCCESS(f"Added allergy {allergy_type.value}."))
            else:
                self.stdout.write(self.style.WARNING(f"Allergy {allergy_type.value} allready exists."))
