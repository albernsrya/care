# Generated by Django 2.2.11 on 2020-03-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="district",
            field=models.IntegerField(choices=[
                (1, "Thiruvananthapuram"),
                (2, "Kollam"),
                (3, "Pathanamthitta"),
                (4, "Alappuzha"),
                (5, "Kottayam"),
                (6, "Idukki"),
                (7, "Ernakulam"),
                (8, "Thrissur"),
                (9, "Palakkad"),
                (10, "Malappuram"),
                (11, "Kozhikode"),
                (12, "Wayanad"),
                (13, "Kannur"),
                (14, "Kasaragod"),
            ]),
        ),
    ]
