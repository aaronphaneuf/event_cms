# Generated by Django 4.1.7 on 2023-04-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0042_prices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prices",
            name="price_1",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_2",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_3",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_4",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_5",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_6",
            field=models.FloatField(),
        ),
    ]
