from django.conf.urls import patterns, url

from Task import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.DetailView.as_view(), name='results'),
    url(r'^(?P<task_id>\d+)/select_proposal/$', views.set_select_proposal, name='set_select_proposal'),

)