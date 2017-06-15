# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-15 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scr', '0009_auto_20170612_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('say', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='time',
            field=models.CharField(default='15/06/17', max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='time',
            field=models.CharField(default='15/06/17', max_length=20),
        ),
    ]
