# Generated by Django 2.2.11 on 2020-10-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0197_auto_20201011_2338"),
    ]

    operations = [
        migrations.AddField(
            model_name="shiftingrequest",
            name="is_assigned_to_user",
            field=models.BooleanField(default=False),
        ),
    ]
