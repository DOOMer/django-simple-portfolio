# coding: utf8

from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
	url(r'^$',  views.ProjectsList.as_view(), name='portfolio-projects-list'),
	url(r'^(?P<slug>[^/]+)/$', views.ProjectDetail.as_view(), name='portfolio-project-detail'),
)