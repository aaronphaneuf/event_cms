# Generated by Django 4.1.7 on 2023-06-16 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0066_alter_pricelayerprice_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discount",
            name="event",
        ),
        migrations.DeleteModel(
            name="Discount2",
        ),
        migrations.AddField(
            model_name="discount",
            name="event",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discount",
                to="core.event",
            ),
            preserve_default=False,
        ),
    ]
