from django.conf.urls import patthern, url

from chat import views

urlpattherns = patthens('',
  url(r'^$', views.home)
)
