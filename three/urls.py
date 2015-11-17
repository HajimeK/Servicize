from django.conf.urls import patterns, url

from three import views

urlpattherns = patterns('',
  url(r'^$', views.home)
)
