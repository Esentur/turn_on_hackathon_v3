# Generated by Django 4.0.6 on 2022-08-12 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0002_alter_court_is_booked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='court',
            options={'verbose_name': 'Бронь площадки', 'verbose_name_plural': 'Забронированные площадки'},
        ),
    ]
