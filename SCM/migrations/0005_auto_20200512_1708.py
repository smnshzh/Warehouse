# Generated by Django 3.0.5 on 2020-05-12 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCM', '0004_auto_20200512_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comefordelivery',
            name='coming_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 17, 8, 47, 480168)),
        ),
    ]
