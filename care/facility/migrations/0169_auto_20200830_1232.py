# Generated by Django 2.2.11 on 2020-08-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0168_auto_20200830_1222"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientconsultation",
            name="admitted_to",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (None, "Not admitted"),
                    (1, "Isolation Room"),
                    (2, "ICU"),
                    (3, "ICU with Ventilator"),
                    (20, "Home Isolation"),
                    (30, "Gynaecology Ward"),
                    (40, "Paediatric Ward"),
                ],
                default=None,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientconsultation",
            name="suggestion",
            field=models.CharField(
                choices=[
                    ("HI", "HOME ISOLATION"),
                    ("A", "ADMISSION"),
                    ("R", "REFERRAL"),
                    ("OP", "OP CONSULTATION"),
                    ("DC", "DOMICILIARY CARE"),
                ],
                max_length=4,
            ),
        ),
    ]
