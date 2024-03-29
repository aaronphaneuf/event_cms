# Generated by Django 4.1.7 on 2023-08-22 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_changelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changelog',
            old_name='change_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='changelog',
            old_name='source',
            new_name='event',
        ),
        migrations.AddField(
            model_name='changelog',
            name='user',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ChangeLogNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('note', models.TextField()),
                ('change_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.changelog')),
            ],
        ),
    ]
