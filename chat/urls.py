from django.conf.urls import patterns, url

from chat import views

urlpatterns = patterns('',
  url(r'^$', views.home),
  url(r'^form/', views.form), 
)
