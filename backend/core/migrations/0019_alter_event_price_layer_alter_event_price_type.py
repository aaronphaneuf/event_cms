# Generated by Django 4.1.7 on 2023-04-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_alter_event_price_layer_alter_event_price_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="price_layer",
            field=models.ManyToManyField(to="core.pricelayer"),
        ),
        migrations.AlterField(
            model_name="event",
            name="price_type",
            field=models.ManyToManyField(to="core.pricetype"),
        ),
    ]
