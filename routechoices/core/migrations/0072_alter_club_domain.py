# Generated by Django 5.1 on 2024-08-13 06:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0071_delete_individualdonator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="domain",
            field=models.CharField(
                blank=True,
                default="",
                max_length=128,
                validators=[
                    django.core.validators.DomainNameValidator(
                        message="Please enter a valid domain"
                    )
                ],
            ),
        ),
    ]
