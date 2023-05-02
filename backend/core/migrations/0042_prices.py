# Generated by Django 4.1.7 on 2023-04-27 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0041_alter_timeslot_time_range"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prices",
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
                ("price_1", models.IntegerField()),
                ("price_2", models.IntegerField()),
                ("price_3", models.IntegerField()),
                ("price_4", models.IntegerField()),
                ("price_5", models.IntegerField()),
                ("price_6", models.IntegerField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="core.event",
                    ),
                ),
                (
                    "price_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.pricetype"
                    ),
                ),
            ],
        ),
    ]