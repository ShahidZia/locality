from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=200, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state_region = models.CharField(max_length=200, blank=True)
    country = CountryField(blank_label='(Select Country)', blank=True)
    phone = models.CharField(max_length=50, blank=True)
    primary_customer_id = models.IntegerField(null=True, blank=True)
    subscription_moniter = models.IntegerField(null=True, blank=True)
    subscription_page = models.IntegerField(null=True, blank=True)
    subscription_price = models.IntegerField(null=True, blank=True)
    subscription_interval = models.CharField(max_length=200, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
