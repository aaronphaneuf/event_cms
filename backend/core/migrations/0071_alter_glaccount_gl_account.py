# Generated by Django 4.1.7 on 2023-07-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_alter_pricetype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glaccount',
            name='gl_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
    ]
