# Generated by Django 4.1.7 on 2023-08-15 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_merge_20230717_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='custom_fields',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='text_field_6',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='text_field_7',
        ),
        migrations.DeleteModel(
            name='CustomTicketFields',
        ),
    ]
