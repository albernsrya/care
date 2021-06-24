# Generated by Django 2.2.11 on 2020-04-15 07:53

from django.db import migrations, transaction

OLD_TO_NEW_FACILITY_TYPE_MAP_LABS = {
    850: 950,
}

OLD_TO_NEW_FACILITY_TYPE_MAP_GOVT_HOSPITALS = {
    200: 800,
    201: 801,
    202: 802,
    203: 803,
    220: 820,
    230: 830,
    231: 831,
    240: 840,
    250: 850,
    260: 860,
    270: 870,
}


def recompute_facility_types(apps, *args):
    facility_model = apps.get_model("facility", "Facility")
    with transaction.atomic():
        for facility in facility_model.objects.filter(facility_type__in=list(
                OLD_TO_NEW_FACILITY_TYPE_MAP_LABS.keys())):
            facility.facility_type = OLD_TO_NEW_FACILITY_TYPE_MAP_LABS[
                facility.facility_type]
            facility.save()

        for facility in facility_model.objects.filter(facility_type__in=list(
                OLD_TO_NEW_FACILITY_TYPE_MAP_GOVT_HOSPITALS.keys())):
            facility.facility_type = OLD_TO_NEW_FACILITY_TYPE_MAP_GOVT_HOSPITALS[
                facility.facility_type]
            facility.save()


def reverse_recompute_facility_types(apps, *args):
    facility_model = apps.get_model("facility", "Facility")
    with transaction.atomic():
        reverse_map = {
            v: k
            for k, v in OLD_TO_NEW_FACILITY_TYPE_MAP_GOVT_HOSPITALS.items()
        }
        for facility in facility_model.objects.filter(
                facility_type__in=list(reverse_map.keys())):
            facility.facility_type = reverse_map[facility.facility_type]
            facility.save()

        reverse_map = {
            v: k
            for k, v in OLD_TO_NEW_FACILITY_TYPE_MAP_LABS.items()
        }
        for facility in facility_model.objects.filter(
                facility_type__in=list(reverse_map.keys())):
            facility.facility_type = reverse_map[facility.facility_type]
            facility.save()


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0094_auto_20200417_1038"),
    ]

    operations = [
        migrations.RunPython(recompute_facility_types,
                             reverse_code=reverse_recompute_facility_types)
    ]
