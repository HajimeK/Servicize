from django.conf.urls import patterns, url

from iot import views

urlpattherns = patterns('',
  url(r'^$', views.home)
)
