# Generated by Django 4.2.4 on 2023-08-22 09:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_event_from_date_remove_event_to_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="event",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="api.event",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="from_day",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="from_month",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(13),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="from_year",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="to_day",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="to_month",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(13),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="to_year",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
    ]
