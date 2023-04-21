# Generated by Django 4.1.7 on 2023-04-20 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_remove_pricelayerprice_event_pricelayerprice_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pricelayerprice",
            name="price_type",
        ),
        migrations.AddField(
            model_name="pricelayerprice",
            name="price_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.pricetype",
            ),
            preserve_default=False,
        ),
    ]
