from django.conf.urls import patterns, url

from three import views

urlpatterns = patterns('',
  url(r'^$', views.home),
)
