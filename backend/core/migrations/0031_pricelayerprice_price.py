# Generated by Django 4.1.7 on 2023-04-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0030_rename_layer_2_layer_pricelayerprice_price_layer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricelayerprice",
            name="price",
            field=models.IntegerField(default=56),
            preserve_default=False,
        ),
    ]
