# Generated by Django 2.2.11 on 2021-06-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0251_auto_20210607_2009"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="medium_sent",
            field=models.IntegerField(choices=[(0, "SYSTEM"), (100, "SMS"),
                                               (200, "WHATSAPP")],
                                      default=0),
        ),
        migrations.AlterField(
            model_name="notification",
            name="event",
            field=models.IntegerField(
                choices=[
                    (0, "MESSAGE"),
                    (20, "PATIENT_CREATED"),
                    (30, "PATIENT_UPDATED"),
                    (40, "PATIENT_DELETED"),
                    (50, "PATIENT_CONSULTATION_CREATED"),
                    (60, "PATIENT_CONSULTATION_UPDATED"),
                    (70, "PATIENT_CONSULTATION_DELETED"),
                    (80, "INVESTIGATION_SESSION_CREATED"),
                    (90, "INVESTIGATION_UPDATED"),
                    (100, "PATIENT_FILE_UPLOAD_CREATED"),
                    (110, "CONSULTATION_FILE_UPLOAD_CREATED"),
                    (120, "PATIENT_CONSULTATION_UPDATE_CREATED"),
                    (130, "PATIENT_CONSULTATION_UPDATE_UPDATED"),
                    (140, "PATIENT_CONSULTATION_ASSIGNMENT"),
                    (200, "SHIFTING_UPDATED"),
                ],
                default=0,
            ),
        ),
    ]
