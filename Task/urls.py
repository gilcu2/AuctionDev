from django.conf.urls import patterns, url

from Task import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<task_id>\d+)/tests/$', views.tests, name='tests'),
    url(r'^(?P<task_id>\d+)/proposals/$', views.proposals, name='proposals'),
)