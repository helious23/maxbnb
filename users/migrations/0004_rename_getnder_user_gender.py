# Generated by Django 3.2.8 on 2021-10-14 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211014_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='getnder',
            new_name='gender',
        ),
    ]
