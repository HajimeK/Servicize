from django.conf.urls import patterns, url

from translate import views

urlpattherns = patterns('',
  url(r'^$', views.home)
)
