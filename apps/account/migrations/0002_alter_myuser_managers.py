# Generated by Django 4.0.6 on 2022-08-10 13:16

import apps.account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', apps.account.models.UserManager()),
            ],
        ),
    ]
