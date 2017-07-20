# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jus', '0004_ju_stop_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ju',
            name='status',
            field=models.CharField(choices=[('active', '活动状态'), ('close', '关闭'), ('delivering', '发货中'), ('paying', '收款中')], default='', max_length=30),
        ),
    ]
