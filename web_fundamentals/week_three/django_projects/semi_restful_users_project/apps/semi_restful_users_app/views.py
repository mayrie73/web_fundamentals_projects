# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "HOORAY GOT TO index route!"
    users = User.objects.all()
    context={
        "users":users
    }
    return render(request,"semi_restful_users_app/index.html", context)
def new(request):
    return render(request,"semi_restful_users_app/new.html")
def create(request):
    user = User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"], 
        email_address = request.POST["email_address"])
    return redirect('/')
def edit(request, id):
    user = User.objects.get(id=id)
    context={"user": user }
    return render(request,"semi_restful_users_app/edit.html", context)
def update( request, id):
    user= User.objects.get(id=id)
    user.first_name= request.POST["first_name"]
    user.last_name= request.POST["last_name"]
    user.email_address= request.POST["email_address"]
    user.save()
    return redirect("/")
def show(request, id):
    user= User.objects.get(id=id)
    context={
        "user":user
    }
    return render(request,"semi_restful_users_app/show.html", context)
def delete(request,id):
    user= User.objects.get(id=id)
    user.delete()
    return redirect("/")
