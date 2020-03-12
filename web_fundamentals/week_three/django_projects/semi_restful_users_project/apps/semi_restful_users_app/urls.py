from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$',views.update),
    url(r'^show/(?P<id>\d+)$', views.show), 
    url(r'^delete/(?P<id>\d+)$', views.delete) 
]