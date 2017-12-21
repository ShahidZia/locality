# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0006_auto_20170723_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='choices',
            field=models.CharField(choices=[(3, 'Upload your page/files'), (2, 'Use the locality wordpress integration'), (1, 'Use an existing landing page or domain'), (4, 'Add pages later')], default='1', max_length=10),
        ),
    ]
