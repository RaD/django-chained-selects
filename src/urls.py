# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('chained_selects.views',
    url(r'^(?P<app_name>[\w\-]+)/(?P<model_name>[\w\-]+)/(?P<method_name>[\w\-]+)/(?P<pk>[\w\-]+)/$', 'filterchain_all', name='filter_all'),
)
