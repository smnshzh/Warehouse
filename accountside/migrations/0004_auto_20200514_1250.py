# Generated by Django 3.0.5 on 2020-05-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountside', '0003_auto_20200513_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='totalaccounts',
            options={'ordering': ('-code',)},
        ),
        migrations.AlterField(
            model_name='accountgroup',
            name='code',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='difinitaccounts',
            name='code',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='totalaccounts',
            name='code',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
