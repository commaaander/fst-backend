# Generated by Django 4.2.9 on 2024-01-10 19:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_eventlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, size=None),
        ),
    ]
