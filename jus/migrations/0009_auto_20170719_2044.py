# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 12:44
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jus', '0008_ju_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ju',
            name='items',
            field=jsonfield.fields.JSONField(),
        ),
    ]
