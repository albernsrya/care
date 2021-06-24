# Generated by Django 2.2.11 on 2020-04-18 17:47

from django.db import migrations


def populate_countries_travelled(*args):
    print("This is no longer needed")
    # from care.facility.management.commands.copy_countries_travelled_old_to_countries_travelled import Command
    # Command.copy_countries_travelled_old()


def reverse_populate_countries_travelled(*args):
    raise Exception(
        "Should manually populate the data and then fake these migrations.")


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0100_auto_20200418_2315"),
    ]

    operations = [
        migrations.RunPython(
            populate_countries_travelled,
            reverse_code=reverse_populate_countries_travelled,
        )
    ]
