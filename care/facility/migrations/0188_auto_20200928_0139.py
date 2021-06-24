# Generated by Django 2.2.11 on 2020-09-27 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0187_patientexternaltest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientexternaltest",
            name="ward",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="users.Ward",
            ),
        ),
    ]
