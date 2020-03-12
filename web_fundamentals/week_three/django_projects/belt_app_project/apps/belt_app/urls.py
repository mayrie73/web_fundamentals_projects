from django.conf.urls import url
from . import views 
from views import *
from django.contrib import messages               
urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^belt_new$', views.belt_new, name= "belt_new"), 
    url(r'^belt_create$', views.belt_create, name ="belt_create"),
    url(r'^belt_show/(?P<id>\d+)$', views.belt_show, name="belt_show"),
    url(r'^belt_remove/(?P<id>\d+)$', views.belt_remove, name="belt_remove"), 
    url(r'^belt_delete/(?P<id>\d+)$',views.belt_delete, name = "belt_delete"), 
]

    
