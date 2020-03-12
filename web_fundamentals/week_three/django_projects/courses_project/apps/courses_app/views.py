# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from ..login_registration_app.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
from time import gmtime, strftime
import re
def index(request):
    print "HOORAY GOT TO index route!"
    user= User.objects.get(id=request.session["id"])
    courses = Course.objects.all()
    context={
        "courses":courses,
        "user":user
    }
    return render(request,"courses_app/index.html", context)
def create(request):
    print "HOORAY GOT TO CREATE ROUTE"
    errors = Course.objects.validate_input(request.POST)
    if (len(errors) > 0):
        for error in errors:
            messages.error(request,error)
        return redirect("/")
    else:
        course = Course.objects.create(
        name=request.POST["name"],
        description=request.POST["description"])
        course.save()
        request.session['id'] = course.id
    return redirect("/new")
def new(request):
    print "Hooray GOT TO NEW ROUTE"
    courses = Course.objects.all()
    context={
        "courses":courses
    }
    return render(request,"courses_app/index.html",context)
def remove(request, id):
    course= Course.objects.get(id=id)
    context={"course": course }
    return render(request,"courses_app/delete.html", context)
def delete(request,id):
    course= Course.objects.get(id=id)
    course.delete()
    return redirect("/")