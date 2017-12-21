from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^preferences$', PreferencesView.as_view(), name='preferences'),
    url(r'^register/', RegistrationView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, name='signin'),
    url(r'^logout$', auth_views.logout, {'next_page': 'login/'}, name='sign_out'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]