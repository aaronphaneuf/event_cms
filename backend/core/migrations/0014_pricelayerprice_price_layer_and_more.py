# Generated by Django 4.1.7 on 2023-04-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_pricelayer_alter_event_price_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricelayerprice",
            name="price_layer",
            field=models.ManyToManyField(to="core.pricelayer"),
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="price_type",
            field=models.ManyToManyField(to="core.pricetype"),
        ),
        migrations.AlterField(
            model_name="event",
            name="price_type",
            field=models.ManyToManyField(to="core.pricetype"),
        ),
    ]
