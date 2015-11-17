from django.conf.urls import patthern, url

from iot import views

urlpattherns = patthens('',
  url(r'^$', views.home)
)
