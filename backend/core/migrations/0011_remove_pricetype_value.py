# Generated by Django 4.1.7 on 2023-04-14 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_remove_pricetype_event_event_price_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pricetype",
            name="value",
        ),
    ]
