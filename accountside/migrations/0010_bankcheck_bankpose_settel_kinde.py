# Generated by Django 3.0.5 on 2020-05-28 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountside', '0009_documentnumber_editable'),
    ]

    operations = [
        migrations.CreateModel(
            name='settel_kinde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='BankPose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True)),
                ('slug', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=40)),
            ],
            options={
                'unique_together': {('name', 'branch')},
            },
        ),
        migrations.CreateModel(
            name='BankCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True)),
                ('slug', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=40)),
            ],
            options={
                'unique_together': {('name', 'branch')},
            },
        ),
    ]
