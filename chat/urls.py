from chat import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', views.home),
  url(r'^chat/(\d*)', views.form), 
)
#urlpatterns = patterns('',
#  url(r'^$', views.home),
#  url(r'^form/', views.form), 
#)
