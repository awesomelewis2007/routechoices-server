# Generated by Django 4.2.4 on 2023-08-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0053_individualdonator"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="list_on_routechoices_com",
            field=models.BooleanField(
                default=True, verbose_name="Listed on Routechoices.com events page"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="privacy",
            field=models.CharField(
                choices=[
                    ("public", "Public"),
                    ("secret", "Secret"),
                    ("private", "Private"),
                ],
                default="public",
                help_text=(
                    "Public: Listed on your club's front page | "
                    "Secret: Can be opened with a link, however not listed on "
                    "frontpage | Private: Only a logged in admin of the club "
                    "can access the page"
                ),
                max_length=8,
            ),
        ),
    ]
