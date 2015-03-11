from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^impressum/$', views.static, {'site' : 'impressum.html'}, name='impressum'),
	#url(r'^konzept/$', views.static, {'site' : 'konzept.html'}, name='konzept'),

	url(r'^send_contactmail/$', views.send_contactmail, name='send_contactmail'),

)
