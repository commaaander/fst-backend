# Generated by Django 4.2.7 on 2023-11-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_parentchildrelationship_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="birthday",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="birthday_members",
                to="api.customdate",
            ),
        ),
    ]
