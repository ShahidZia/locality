# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0009_campaigns_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='optimize',
            field=models.CharField(choices=[('2', 'North America'), ('3', 'Europe'), ('4', 'Asia/Oceania'), ('1', 'South America')], default='1', max_length=10),
        ),
    ]
