# Generated by Django 3.0.5 on 2020-06-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountside', '0017_safe_box'),
        ('UserControl', '0011_access_accounting_after_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='box',
            field=models.ManyToManyField(to='accountside.Safe_Box'),
        ),
    ]
