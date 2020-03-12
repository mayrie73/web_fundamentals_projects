# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import re
import bcrypt
from django.contrib.auth.views import login

# Create your views here.
def index(request):
    print "HOORAY GOT TO index route!"
    users = User.objects.all()
    context={
        "users":users
    }
    return render(request,"login_registration_app/index.html", context)
def create(request):
    print "HOORAY GOT TO CREATE ROUTE"
    errors = User.objects.validate_input(request.POST)
    if (len(errors) > 0):
        for error in errors:
            messages.error(request,error)
        return redirect("/")
    else:
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"], 
        email= request.POST["email"],
        password= hashed_password)
        user.save()
        request.session['id'] = user.id
    return redirect("/success")
def success(request):
    user= User.objects.get(id=request.session["id"])
    context={
        "user":user
    }
    return render(request,"login_registration_app/success.html", context)
def login(request):
    print "HOORAY GOT TO LOGIN ROUTE"
    errors = User.objects.validate_login(request.POST)
    if (errors) > 0:
        for error in errors:
            messages.error(request,error)
        return redirect("/")
    else:
        user = (User.objects.filter(email=request.POST['email'])).first()
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        request.session['id'] = user.id
        return redirect('/success')  
def log_out(request):
    request.session.clear()
    return redirect('/')

