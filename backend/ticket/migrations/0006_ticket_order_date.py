# Generated by Django 4.1.7 on 2023-08-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_remove_ticket_custom_fields_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='order_date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
