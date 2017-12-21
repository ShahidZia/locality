# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import URLValidator
from django.db import models

# Create your models here.
from Customer.models import Profile


class Campaigns(models.Model):

  created = models.DateTimeField(auto_now=True,blank=True)
  customer = models.ForeignKey(Profile,blank=True)
  name = models.CharField(max_length=60,blank=True)
  notes = models.TextField(max_length=500, blank=True)
  choice = {
      ('1', 'Personal'),
      ('2', 'Private'),
      ('3', 'Public'),
  }
  choices = models.CharField(max_length=10, choices=choice,default='1')

class LandingPage(models.Model):
    optimzie_for = {
        ('1', 'South America'),
        ('2', 'North America'),
        ('3', 'Europe'),
        ('4', 'Asia/Oceania'),
    }
    name = models.CharField(max_length=30,blank=True)
    origin = models.CharField(validators=[URLValidator],max_length=40)
    campain = models.ForeignKey(Campaigns,null=True)
    domain_id = models.CharField(max_length=30, blank=True)
    optimize = models.CharField(max_length=10, choices=optimzie_for, default='1')
    type = models.CharField(max_length=30, blank=True)
    avg_perf = models.CharField(max_length=30, blank=True)
    avg_grade = models.CharField(max_length=30, blank=True)
    perf_improve = models.CharField(max_length=30, blank=True)
    avg_visitor = models.CharField(max_length=30, blank=True)
    visitor_per_day = models.IntegerField(null=True, blank=True)
    total_visitor = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True,editable=False)
    modified = models.DateTimeField(auto_now=True)
    choice = {
        ('active','Active'),
        ('disable', 'Disable'),
    }
    status = models.CharField(max_length=10,choices=choice,blank=True)