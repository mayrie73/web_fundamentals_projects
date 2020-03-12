from django.conf.urls import url
from . import views 
from django.contrib import messages      
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.process),
    url(r'^refresh$', views.refresh), 
]

