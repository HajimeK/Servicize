from django.conf.urls import patterns, url

from chat import views

urlpattherns = patterns('',
  url(r'^$', views.home)
)
