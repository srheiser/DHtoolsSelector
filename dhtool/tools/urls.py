from django.conf.urls import url

from . import views

urlpatterns = [
#	url(r'^$', views.index, name='index'),
	url(r'^$', views.project, name='project'),
	url(r'^project/(?P<id>[0-9]+)/$', views.project_userstory, name='project_userstory'),
	url(r'^mappingtool/(?P<id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^userstory/(?P<id>[0-9]+)/$', views.userstory, name='userstory'),
	url(r'^result',views.result, name='result'),
]
