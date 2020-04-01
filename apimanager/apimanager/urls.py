# -*- coding: utf-8 -*-
"""
URLs for apimanager
"""

from django.conf.urls import url, include
from django.contrib import admin
from base.views import HomeView
from obp.views import (
    OAuthInitiateView, OAuthAuthorizeView,
    DirectLoginView,
    GatewayLoginView,
    LogoutView,
)


urlpatterns = [
    # This will open the admin portal 
    url('admin/', admin.site.urls),# should always use include(), this is the only exception. 
    url(r'^$', HomeView.as_view(), name="home"),
    # Defining authentication URLs here and not including oauth.urls for
    # backward compatibility
    url(r'^oauth/initiate$',
        OAuthInitiateView.as_view(), name='oauth-initiate'),
    url(r'^oauth/authorize$',
        OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    url(r'^directlogin$',
        DirectLoginView.as_view(), name='directlogin'),
    url(r'^gatewaylogin$',
        GatewayLoginView.as_view(), name='gatewaylogin'),
    url(r'^logout$',
        LogoutView.as_view(), name='oauth-logout'),
    url(r'^consumers/', include('consumers.urls')),
    url(r'^entitlementrequests/', include('entitlementrequests.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^branches/', include('branches.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^metrics/', include('metrics.urls')),
    url(r'^config/', include('config.urls')),
    url(r'^webui/', include('webui.urls')),
    url(r'^methodrouting/', include('methodrouting.urls')),
    url(r'^dynamicendpoints/', include('dynamicendpoints.urls')),
]
