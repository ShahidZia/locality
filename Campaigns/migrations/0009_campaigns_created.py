# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0008_auto_20170723_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
