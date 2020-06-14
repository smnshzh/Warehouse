# Generated by Django 3.0.5 on 2020-05-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_inventory_warehousedefinde'),
        ('UserControl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='access',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='access',
            name='warehouse',
            field=models.ManyToManyField(to='Shop.WareHouseDefinde'),
        ),
    ]
