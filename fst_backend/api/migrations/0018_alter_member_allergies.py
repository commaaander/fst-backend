# Generated by Django 4.2.4 on 2023-08-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_rename_allergies_allergy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="allergies",
            field=models.ManyToManyField(blank=True, null=True, to="api.allergy"),
        ),
    ]