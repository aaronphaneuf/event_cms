# Generated by Django 4.1.7 on 2023-04-21 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0034_alter_glaccount_event"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("discount", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                (
                    "event",
                    models.ManyToManyField(related_name="discount", to="core.event"),
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
