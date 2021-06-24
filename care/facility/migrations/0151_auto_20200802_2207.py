# Generated by Django 2.2.11 on 2020-08-02 16:37

import django.core.validators
import fernet_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0150_auto_20200802_2156"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="name_old",
            field=fernet_fields.fields.EncryptedCharField(default="",
                                                          max_length=200),
        ),
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="phone_number_old",
            field=fernet_fields.fields.EncryptedCharField(
                default="",
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message=
                        "Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="name_old",
            field=fernet_fields.fields.EncryptedCharField(default="",
                                                          max_length=200),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="phone_number_old",
            field=fernet_fields.fields.EncryptedCharField(
                default="",
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message=
                        "Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
            ),
        ),
    ]
