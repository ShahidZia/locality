from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address1', 'address2', 'city', 'country', 'phone')
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'})
        }

class ProfileForm(forms.Form):

    name = forms.CharField(required=True)