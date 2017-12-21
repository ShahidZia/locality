# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0003_auto_20170721_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('notes', models.TextField(blank=True, max_length=500)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('origin', models.URLField(blank=True)),
                ('domain_id', models.CharField(blank=True, max_length=30)),
                ('type', models.CharField(blank=True, max_length=30)),
                ('avg_perf', models.CharField(blank=True, max_length=30)),
                ('avg_grade', models.CharField(blank=True, max_length=30)),
                ('perf_improve', models.CharField(blank=True, max_length=30)),
                ('avg_visitor', models.CharField(blank=True, max_length=30)),
                ('visitor_per_day', models.IntegerField(blank=True, null=True)),
                ('total_visitor', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('active', 'Active'), ('disable', 'Disable')], max_length=10)),
            ],
        ),
    ]
