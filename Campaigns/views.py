# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from Campaigns.forms import CampaignsAddForm, CampaignsLandingForm
from Campaigns.models import Campaigns
from Customer.models import Profile
import csv, six

class CampaignsView(LoginRequiredMixin, View):
    template_name = 'Campaigns/campaigns.html'


    def get(self, request, *args, **kwargs):
        compaign_objects = Campaigns.objects.filter(customer_id=request.user.id).order_by('-created')
        return render(request, self.template_name,{'compaign_objects':compaign_objects})


class ImportData(LoginRequiredMixin, View):
    template_name = 'admin/new_html.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        if request.FILES:
            message = create_campaigns_through_csv(request.FILES.get("fileToUpload"))
            return render(request, self.template_name, {'message':message})


def create_campaigns_through_csv(csvfile):
    message = ''
    columns = 3
    Campaigns_list = []
    errors = []
    for index, line in enumerate(csv.reader(csvfile)):
        if len(line) != columns:
            return 'Incorrect columns structure. It must contains 3 columns and be in profile_id , notes, name format.'
        customer, notes, name = line
        campaign = {}
        campaign['name'] = name
        campaign['notes'] = notes
        campaign['customer'] = customer

        if campaign['customer']:
            if not Profile.objects.filter(id=campaign['customer']).exists():
                return 'Profile for Id: {} - wasn\'t found.\n' \
                    .format(
                    campaign['customer'])
            else:
                campaign['customer'] = Profile.objects.get(id=campaign['customer'])
        else:
            return 'Please provide profile id.'

        data = QueryDict('', mutable=True)
        data.update(campaign)
        form = CampaignsAddForm(data)

        if not form.is_valid():
            errors.append(
                'Row: {} Followed errors has been found in file: {}\n'
                    .format(
                    index + 1,
                    ', '.join(
                        '{}: {}'.format(field, ', '.join(error)) for
                        field, error in form.errors.iteritems()
                    )
                )
            )
        else:
            campaign['name'] = form.cleaned_data['name']
            campaign['notes'] = form.cleaned_data['notes']

            Campaigns_list.append(campaign)

    if errors:
        return '\n'.join(errors)

    for camp in Campaigns_list:
        message += 'Creating Campaign for {}... \n'.format(camp['name'])

        Campaigns.objects.create(customer=camp['customer'], name=camp['name'], notes=camp['notes'])
        message += 'Created Campaign: {} successfully\n'.format(camp['name'])
        message += '==================================================\n'

    return message

class CampaignsAdd(LoginRequiredMixin, View):
    form_class = CampaignsAddForm
    template_name = 'Campaigns/campaigns_add.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            forms = form.instance
            forms.customer_id = Profile.objects.get(id=request.user.id).id
            forms.save()
            if forms.choices == '4':
                return redirect('campaigns_thank_you', id=self.kwargs['id'])
            elif forms.choices == '1':
                return redirect('campaigns_landing_page', id=self.kwargs['id'])

        return render(request, 'Campaigns/campaigns_add.html', {'form': form})

class CampaignsEdit(LoginRequiredMixin, View):
    form_class = CampaignsAddForm
    template_name = 'Campaigns/campaigns_add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=Campaigns.objects.get(id=self.kwargs['id']))

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,instance=Campaigns.objects.get(id=self.kwargs['id']))
        if form.is_valid():
            forms = form.instance
            forms.save()
            if forms.choices == '4':
                return redirect('campaigns_thank_you', id=self.kwargs['id'])
            elif forms.choices == '1':
                return redirect('campaigns_landing_page', id=self.kwargs['id'])

        return render(request, 'Campaigns/campaigns_add.html', {'form': form})


class CampaignsThankYou(LoginRequiredMixin,View):
    template_name = 'Campaigns/campaign_thankyou.html'

    def get(self, request, *args, **kwargs):
        get_obj = Campaigns.objects.get(id=self.kwargs['id'])
        get_prof = Profile.objects.get(id=get_obj.customer_id)
        return render(request, self.template_name, {'object': get_obj,'prof_obj':get_prof})

class CampaignsLandingPage(LoginRequiredMixin,View):
    form_class = CampaignsLandingForm
    template_name = 'Campaigns/campaign_landing_page.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=Campaigns.objects.get(id=self.kwargs['id']))
        if form.is_valid():
            forms = form.instance
            forms.save()


        return render(request, 'Campaigns/campaigns_add.html', {'form': form})
