#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^impressum/$', views.static, {'site' : 'impressum.html'}, name='impressum'),

	url(r'^send_contactmail/$', views.send_contactmail, name='send_contactmail'),
	url(r'^set_wish_ordered/$', views.set_wish_ordered, name='set_wish_ordered'),
	url(r'^reset_ordered_form/$', views.reset_ordered_form, name='reset_ordered_form'),

)
