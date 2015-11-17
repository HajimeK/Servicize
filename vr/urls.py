from django.conf.urls import patterns, url

from vr import views

urlpattherns = patterns('',
  url(r'^$', views.home)
)
