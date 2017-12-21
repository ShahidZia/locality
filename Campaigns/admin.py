# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http import HttpResponse
import decimal, csv
# Register your models here.
from .models import *


def export_campaign(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="campaign.csv"'
    writer = csv.writer(response)
    writer.writerow(['customer','notes', 'name', 'choices'])
    campagin = queryset.values_list('customer','notes', 'name', 'choices')
    for campagins in campagin:
        writer.writerow(campagins)
    return response
export_campaign.short_description = 'Export to csv'

class CampaginAdmin(admin.ModelAdmin):
    list_display = ['customer','notes', 'name', 'choices']
    actions = [export_campaign, ]

admin.site.register(Campaigns, CampaginAdmin)

