# Generated by Django 4.1.7 on 2023-05-11 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0052_remove_discount_event_discount_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.event"
            ),
        ),
    ]