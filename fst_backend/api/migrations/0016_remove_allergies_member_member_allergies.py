# Generated by Django 4.2.4 on 2023-08-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_alter_member_diettype_allergies"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="allergies",
            name="member",
        ),
        migrations.AddField(
            model_name="member",
            name="allergies",
            field=models.ManyToManyField(to="api.allergies"),
        ),
    ]