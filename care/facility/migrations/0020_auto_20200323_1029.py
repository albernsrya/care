# Generated by Django 2.2.11 on 2020-03-23 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0019_auto_20200322_2056"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="facilitycapacity",
            unique_together={("facility", "room_type", "deleted")},
        ),
        migrations.AlterUniqueTogether(
            name="hospitaldoctors",
            unique_together={("facility", "area", "deleted")},
        ),
    ]
