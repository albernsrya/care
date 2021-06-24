# Generated by Django 2.2.11 on 2020-04-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0075_auto_20200405_1122"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientsample",
            name="atypical_presentation",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="diagnosis",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="diff_diagnosis",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="doctor_name",
            field=models.CharField(default="NO DOCTOR SPECIFIED",
                                   max_length=255),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="etiology_identified",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="has_ari",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="has_sari",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="is_atypical_presentation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="is_unusual_course",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="sample_type",
            field=models.IntegerField(
                choices=[
                    (0, "UNKNOWN"),
                    (1, "BA/ETA"),
                    (2, "TS/NPS/NS"),
                    (3, "Blood in EDTA"),
                    (4, "Acute Sera"),
                    (5, "Covalescent sera"),
                    (6, "OTHER TYPE"),
                ],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="patientsample",
            name="sample_type_other",
            field=models.TextField(default=""),
        ),
    ]
