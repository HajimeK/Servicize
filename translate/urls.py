from django.conf.urls import patthern, url

from translate import views

urlpattherns = patthens('',
  url(r'^$', views.home)
)
