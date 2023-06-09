# Generated by Django 4.1.7 on 2023-04-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_alter_pricelayerprice_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pricelayerprice",
            name="event",
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="event",
            field=models.ManyToManyField(
                related_name="price_layer_price", to="core.event"
            ),
        ),
    ]
