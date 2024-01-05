from django.core.management.base import BaseCommand
from fst_backend.api.models import Allergy


class Command(BaseCommand):
    help = "Initialize database with some base content (e.g. allergy types)"

    def handle(self, *args, **options):
        self.stdout.write("Init allergy database.")
        type_already_exists_count = 0
        for allergy_type in Allergy.AllergyType:
            if not Allergy.objects.filter(type=allergy_type.value).exists():
                Allergy.objects.create(type=allergy_type.value)
                self.stdout.write(self.style.SUCCESS(f"Added allergy type {allergy_type.value}."))
            else:
                type_already_exists_count += 1

        if type_already_exists_count > 0:
            self.stdout.write(self.style.WARNING(f"{type_already_exists_count} allergy types already existed."))
