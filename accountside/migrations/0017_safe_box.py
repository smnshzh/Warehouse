# Generated by Django 3.0.5 on 2020-06-07 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountside', '0016_geoaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Safe_Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('accountside', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountside.accountside')),
            ],
        ),
    ]
