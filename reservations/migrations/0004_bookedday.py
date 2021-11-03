# Generated by Django 3.2.8 on 2021-11-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20211016_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
            options={
                'verbose_name': 'Booked Day',
                'verbose_name_plural': 'Booked Days',
            },
        ),
    ]
