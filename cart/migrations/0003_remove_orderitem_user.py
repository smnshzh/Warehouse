# Generated by Django 3.0.5 on 2020-05-11 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
