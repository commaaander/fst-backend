# Generated by Django 4.2.5 on 2023-09-25 19:56

from django.db import migrations, models
import fst_backend.api.models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_alter_member_allergies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventmedia",
            name="mediaUrl",
            field=models.ImageField(
                blank=True, null=True, upload_to=fst_backend.api.models.upload_to
            ),
        ),
    ]