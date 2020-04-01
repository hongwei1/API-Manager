# -*- coding: utf-8 -*-
"""
URLs for users app
"""

from django.conf.urls import url

from .views import IndexView, DetailView, MyDetailView, DeleteEntitlementView

urlpatterns = [
    url(
        r'^all$', # URL!
        # as_view() from the TemplateView, 
        # you do not need to write the`render(request, '/path/to/template.html')` again..   
        IndexView.as_view(), # view, method !
        name='users-index' # namespace!
        ),
    url(r'^all/user_id/(?P<user_id>[\w\@\.\+-]+)$',
        DetailView.as_view(),
        name='users-detail'),
    url(r'^myuser/user_id/(?P<user_id>[\w\@\.\+-]+)$',
        MyDetailView.as_view(),
        name='my-user-detail'),
    url(r'^(?P<user_id>[\w-]+)/entitlement/delete/(?P<entitlement_id>[\w-]+)$',
        DeleteEntitlementView.as_view(),
        name='users-delete-entitlement'),
]
