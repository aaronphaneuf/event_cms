# Generated by Django 4.1.7 on 2023-07-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_remove_discount_event_delete_discount2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountlayer',
            name='event',
        ),
        migrations.AddField(
            model_name='accountlayer',
            name='event',
            field=models.ManyToManyField(related_name='account', to='core.event'),
        ),
    ]
