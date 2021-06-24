# Generated by Django 2.2.11 on 2020-04-02 21:49

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0067_auto_20200402_1841"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="admitted_to",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (None, "Not admitted"),
                    (1, "Isolation Room"),
                    (2, "ICU"),
                    (3, "ICU with Ventilator"),
                ],
                default=None,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Mild", "Category-A"),
                    ("Moderate", "Category-B"),
                    ("Severe", "Category-C"),
                    (None, "UNCLASSIFIED"),
                ],
                default=None,
                max_length=8,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="other_symptoms",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="symptoms",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    (1, "ASYMPTOMATIC"),
                    (2, "FEVER"),
                    (3, "SORE THROAT"),
                    (4, "COUGH"),
                    (5, "BREATHLESSNESS"),
                    (6, "MYALGIA"),
                    (7, "ABDOMINAL DISCOMFORT"),
                    (8, "VOMITING/DIARRHOEA"),
                    (9, "OTHERS"),
                ],
                default=1,
                max_length=17,
            ),
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="symptoms_onset_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="patientteleconsultation",
            name="symptoms",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    (1, "ASYMPTOMATIC"),
                    (2, "FEVER"),
                    (3, "SORE THROAT"),
                    (4, "COUGH"),
                    (5, "BREATHLESSNESS"),
                    (6, "MYALGIA"),
                    (7, "ABDOMINAL DISCOMFORT"),
                    (8, "VOMITING/DIARRHOEA"),
                    (9, "OTHERS"),
                ],
                max_length=17,
            ),
        ),
    ]
