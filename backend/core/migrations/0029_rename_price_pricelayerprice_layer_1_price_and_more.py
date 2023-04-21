# Generated by Django 4.1.7 on 2023-04-20 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_remove_pricelayerprice_price_layer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pricelayerprice",
            old_name="price",
            new_name="layer_1_price",
        ),
        migrations.RenameField(
            model_name="pricelayerprice",
            old_name="price_layer",
            new_name="layer_2_layer",
        ),
        migrations.RenameField(
            model_name="pricelayerprice",
            old_name="price_type",
            new_name="layer_2_type",
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="layer_1_layer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="layer_1_layer",
                to="core.pricelayer",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="layer_1_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="layer_1_type",
                to="core.pricetype",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="layer_2_price",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
