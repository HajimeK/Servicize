from django.conf.urls import patterns, url

from iot import views

urlpatterns = patterns('',
  url(r'^$', views.home),
)
