# Generated by Django 5.0 on 2023-12-29 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersurls',
            old_name='url',
            new_name='url_large',
        ),
        migrations.RenameField(
            model_name='usersurls',
            old_name='label',
            new_name='url_small',
        ),
    ]
