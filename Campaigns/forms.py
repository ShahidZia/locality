from django import forms
from .models import *


class CampaignsAddForm(forms.ModelForm):

    class Meta:
        model = Campaigns
        fields = ('name', 'notes',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'col':3, 'rows': 4,'class': 'form-control'}),
        }

class CampaignsLandingForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = ('name', 'origin', 'domain_id','optimize')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'optimize': forms.Select(attrs={'class': 'form-control'}),
            'domain_id': forms.Textarea(attrs={'class': 'form-control'})
        }
