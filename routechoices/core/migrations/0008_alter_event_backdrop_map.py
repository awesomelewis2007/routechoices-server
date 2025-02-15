# Generated by Django 4.0.4 on 2022-04-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_device_battery_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="backdrop_map",
            field=models.CharField(
                choices=[
                    ("blank", "Blank"),
                    ("osm", "Open Street Map"),
                    ("gmap-street", "Google Map Street"),
                    ("gmap-hybrid", "Google Map Satellite"),
                    ("mapant-fi", "Mapant Finland"),
                    ("mapant-no", "Mapant Norway"),
                    ("mapant-es", "Mapant Spain"),
                    ("topo-fi", "Topo Finland"),
                    ("topo-no", "Topo Norway"),
                    ("topo-uk", "Topo UK"),
                    ("topo-world", "Topo World (OpenTopo)"),
                    ("topo-world-alt", "Topo World (ArcGIS)"),
                ],
                default="blank",
                max_length=16,
            ),
        ),
    ]
