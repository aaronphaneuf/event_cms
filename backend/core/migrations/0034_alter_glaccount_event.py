# Generated by Django 4.1.7 on 2023-04-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0033_glaccount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glaccount",
            name="event",
            field=models.ManyToManyField(related_name="gl_account", to="core.event"),
        ),
    ]
