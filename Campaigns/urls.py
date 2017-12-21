from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^campaigns/$', CampaignsView.as_view(), name='campaigns'),
    url(r'^spreadsheet$', ImportData.as_view(), name='import_data'),
    url(r'^campaigns_add/$', CampaignsAdd.as_view(), name='campaigns_add'),
    url(r'^campaigns_edit/(?P<id>[0-9]+)/$', CampaignsEdit.as_view(), name='campaigns_edit'),
    url(r'^campaigns_thank_you/(?P<id>[0-9]+)/$', CampaignsThankYou.as_view(), name='campaigns_thank_you'),
    url(r'^campaigns_landing_page/(?P<id>[0-9]+)/$', CampaignsLandingPage.as_view(), name='campaigns_landing_page'),
]