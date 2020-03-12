# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import Author, Book , Review
from ..login_registration_app.models import User
from django.db.models import Count

# Create your views here.
def index(request):
    print "HOORAY GOT TO index route!"
    user= User.objects.get(id=request.session["id"])
    authors = Author.objects.all()
    reviews= Review.objects.order_by('created_at')[:3]
    books = Book.objects.order_by('created_at')[:3]
    context={
        "user":user,
        "reviews":reviews,
        "books": books,
        "authors": authors
    }
    return render(request,"book_app/index.html", context)
def book_create(request):
    print"HOORAY GOT TO CREATE ROUTE"
    if len(request.POST["new_author"])== 0:
        author=Author.objects.get(id=request.POST["author"])
    else:
        print "Trying to create an author"
        author=Author.objects.create(name=request.POST["new_author"])
    user = User.objects.get(id=request.session['id'])
    book=Book.objects.create(title=request.POST['title'], author=author, user=user)
    Review.objects.create(review=request.POST['review'], rating = request.POST['rating'], user =user, book=book)
    return redirect("/book")
def book_add(request):
    print"HOORAY GOT TO BOOK ADD ROUTE!!!"
    return render(request,"book_app/book_add.html")
def user_views(request):
    print "HOORAY GOT TO USER REVIEWS ROUTE!!!"
    return render(request,"book_app/user_reviews.html")
def book_reviews(request):
    print"HOORAY GOT TO BOOK REVIEWS ROUTE"
    review = Review.objects.order_by('created_at')[:3]
    context = {'review': review}
    return render(request,"book_app/book_reviews.html",context)
def delete(request):
    print "HOORAY GOT TO DELETE ROUTE"
    return redirect('/book/book_reviews')

