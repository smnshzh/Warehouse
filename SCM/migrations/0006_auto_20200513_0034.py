# Generated by Django 3.0.5 on 2020-05-12 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCM', '0005_auto_20200512_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comefordelivery',
            name='coming_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 0, 33, 47, 831732)),
        ),
    ]
