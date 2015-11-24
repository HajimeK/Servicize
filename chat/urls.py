from django.conf.urls import patterns, url

from chat import views

urlpatterns = patterns('Serviceize2',
  url(r'^$', views.home),
  url(r'^chat/(\d*)', views.form), 
)
#urlpatterns = patterns('',
#  url(r'^$', views.home),
#  url(r'^form/', views.form), 
#)