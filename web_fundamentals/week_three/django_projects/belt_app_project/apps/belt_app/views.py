from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import * 
from ..login_registration_app.models import User
from time import gmtime, strftime
# Create your views here.
def index(request):
    print "HOORAY GOT TO index route!"
    users = User.objects.all()
    user = User.objects.get(id=request.session['id'])
    products = Product.objects.all()
    context={
        "user":user,
        "users":users,
        "products": products,
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    return render(request,"belt_app/index.html",context)
def belt_new(request):
    print "GOT TO NEW ROUTE"
    if not "id" in request.session:
        message.error(request, "You must be logged in to add item!")
        return redirect("/")
    return render(request,"belt_app/belt_new.html")
def belt_create(request):
    print "GOT TO CREATE ROUTE"
    errors = Product.objects.validate_input(request.POST)
    if (len(errors) > 0):
        for error in errors:
            messages.error(request,error)
        return redirect("/belt/belt_new")
    else:
        current_user = User.objects.get(id=request.session['id'])
        new_product= Product.objects.create(item=request.POST['item'], creator = current_user)
        return redirect("/belt")
def belt_show(request, id):
    print "GOT TO SHOW ROUTE"
    user= User.objects.get(id=request.session["id"])
    products=Product.objects.filter(id=id)
    context={
    "products": products,
    "user":user 
    }
    return render(request,"belt_app/belt_show.html", context)
def belt_remove(request, id):
    print "GOT TO REMOVE ROUTE"
    context = {
        'product': Product.objects.get(id = id)
    }
    return render(request,"belt_app/belt_delete.html", context)  
def belt_delete(request, id):
    print "GOT TO DELETE ROUTE"
    user = User.objects.get(id = request.session['id'])
    product= Product.objects.get(id = id)
    Product.objects.get(id = id).delete()
    return redirect("/belt")

 


