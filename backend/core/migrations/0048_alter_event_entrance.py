# Generated by Django 4.1.7 on 2023-04-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_alter_event_entrance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="entrance",
            field=models.CharField(
                choices=[
                    ("North Entrance", "North"),
                    ("South Entrance", "South"),
                    ("West Entrance", "West"),
                ],
                default="NORTH_ENTRANCE",
                max_length=14,
            ),
        ),
    ]
