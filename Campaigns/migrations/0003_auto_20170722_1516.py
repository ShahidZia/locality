# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0002_auto_20170722_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaigns',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
