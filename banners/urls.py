# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('banners.views',
                       url(regex=r'^placement/(?P<placement_id>\d+)/(?P<zone_id>\d+)/$', view='placement',
                           name='placement'),
                       url(regex=r'^view/(?P<banner_id>\d+)/(?P<zone_id>\d+)/(?P<btype>img|swf)/$',
                           view='shows', name='shows'),
                       url(regex=r'^click/(?P<banner_id>\d+)/(?P<zone_id>\d+)/$',
                           view='clicks', name='clicks'),
                       url(regex=r'^code/(?P<zone_id>\d+)/(?P<btype>ip|name)/$',  view='code', name='code'),
                       url(regex=r'^zones/$',  view='code', name='zones'),
)