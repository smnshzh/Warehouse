# Generated by Django 3.0.5 on 2020-05-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20200518_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='code',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
