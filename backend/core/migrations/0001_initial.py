# Generated by Django 4.1.7 on 2023-04-13 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("capacity", models.IntegerField()),
                ("held", models.IntegerField()),
                (
                    "entrance",
                    models.CharField(
                        choices=[("N", "North"), ("S", "South"), ("W", "West")],
                        default="NORTH_ENTRANCE",
                        max_length=1,
                    ),
                ),
                (
                    "gr_required",
                    models.CharField(
                        choices=[("Y", "Yes"), ("N", "No")],
                        default="NO_CHOICE",
                        max_length=1,
                    ),
                ),
                (
                    "early_closure",
                    models.CharField(
                        choices=[("Y", "Yes"), ("N", "No")],
                        default="NO_CHOICE",
                        max_length=1,
                    ),
                ),
                (
                    "csi_needed",
                    models.CharField(
                        choices=[("Y", "Yes"), ("N", "No")],
                        default="NO_CHOICE",
                        max_length=1,
                    ),
                ),
                (
                    "csi_mandatory",
                    models.CharField(
                        choices=[("Y", "Yes"), ("N", "No")],
                        default="NO_CHOICE",
                        max_length=1,
                    ),
                ),
                ("csi_notes", models.TextField()),
                ("additional_notes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="PriceLayerPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PriceTypeLayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price_type_layer_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="DateTime",
            fields=[
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.event",
                    ),
                ),
                ("event_date", models.DateField()),
                ("event_time", models.TimeField()),
                ("door_open", models.TimeField()),
                ("door_close", models.TimeField()),
                ("sell_date", models.DateField()),
                ("sell_time", models.TimeField()),
                ("stop_date", models.DateTimeField()),
                ("stop_time", models.TimeField()),
                ("early_closure_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_range", models.CharField(max_length=255)),
                ("capacity", models.IntegerField()),
                ("held", models.IntegerField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PriceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price_type_name", models.CharField(max_length=255)),
                (
                    "price_layer",
                    models.ManyToManyField(null=True, to="core.pricetypelayer"),
                ),
                ("value", models.ManyToManyField(null=True, to="core.pricelayerprice")),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_name", models.CharField(max_length=255)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.event"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facility_name", models.CharField(max_length=255)),
                (
                    "event",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.event",
                    ),
                ),
            ],
        ),
    ]
