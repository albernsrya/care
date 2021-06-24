# Generated by Django 2.2.11 on 2020-04-09 06:31

import fernet_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0080_auto_20200409_0459"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientSearch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient_id", fernet_fields.fields.EncryptedIntegerField()),
                ("name", models.CharField(max_length=120)),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(1, "Male"), (2, "Female"), (3,
                                                              "Non-binary")]),
                ),
                ("phone_number", models.CharField(max_length=14)),
                ("date_of_birth", models.DateField(null=True)),
                ("year_of_birth", models.IntegerField()),
                ("state_id", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="date_of_birth",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="year_of_birth",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="date_of_birth",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="patient_search_id",
            field=fernet_fields.fields.EncryptedIntegerField(
                help_text="FKey to PatientSearch", null=True),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="year_of_birth",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddIndex(
            model_name="patientsearch",
            index=models.Index(
                fields=["year_of_birth", "date_of_birth", "phone_number"],
                name="facility_pa_year_of_cf9f3e_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="patientsearch",
            index=models.Index(
                fields=["year_of_birth", "phone_number"],
                name="facility_pa_year_of_c04a3d_idx",
            ),
        ),
    ]
