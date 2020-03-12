from django.conf.urls import url
from . import views 
from views import *
from django.contrib import messages               
urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^book_add$', views.book_add, name="book_add"),
    url(r'^user_views$', views.user_views, name="user_views"), 
    url(r'^book_reviews$', views.book_reviews, name="book_reviews"), 
    url(r'^book_create$', views.book_create, name="book_create"), 
    url(r'^delete$', views.delete, name="delete"),

]