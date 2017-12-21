import csv, six

from django.contrib.auth import login, authenticate
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from .forms import RegisterForm,ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import *

class RegistrationView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'Customer/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')

        return render(request, self.template_name, {'form': form})


class DashboardView(LoginRequiredMixin, View):
    template_name = 'Customer/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class PreferencesView(LoginRequiredMixin, View):
    form_class = ProfileForm
    template_name = 'Customer/preferences.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=Profile.objects.get(user=request.user))
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            # return redirect('preferences')

        return render(request, self.template_name, {'form': form})