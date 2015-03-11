#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^impressum/$', views.static, {'site' : 'impressum.html'}, name='impressum'),

	url(r'^send_contactmail/$', views.send_contactmail, name='send_contactmail'),

)
