# Generated by Django 4.1.7 on 2023-05-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0058_accounts_accountlayer"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Accounts",
            new_name="Account",
        ),
    ]
