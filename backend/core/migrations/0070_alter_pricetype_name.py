# Generated by Django 4.1.7 on 2023-07-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_rename_account_accountlayer_gl_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricetype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]