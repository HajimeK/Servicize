from django.conf.urls import patterns, url

from vr import views

urlpatterns = patterns('',
  url(r'^$', views.home),
)
