# Generated by Django 4.1.7 on 2023-07-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_customticketfields_remove_ticket_custom_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='custom_fields',
        ),
        migrations.AddField(
            model_name='ticket',
            name='custom_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='CustomTicketFields',
        ),
    ]