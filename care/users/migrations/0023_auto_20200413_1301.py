# Generated by Django 2.2.11 on 2020-04-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0022_auto_verify_users_with_facility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.IntegerField(choices=[
                (5, "Doctor"),
                (10, "Staff"),
                (15, "Patient"),
                (20, "Volunteer"),
                (25, "DistrictLabAdmin"),
                (30, "DistrictAdmin"),
                (35, "StateLabAdmin"),
                (40, "StateAdmin"),
            ]),
        ),
    ]
