# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "HOORAY GOT TO index route!"
    return render(request,"user_login_app/index.html")
def new(request):
    return render(request,"user_login_app/new.html")
def create(request):
    print "Got to create route"
    new_user = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"], email = request.POST["email"], age = request.post["age"], created_at = request.POST["created_at"], updated_at= request.POST["updated_at"])
    return redirect('/')
