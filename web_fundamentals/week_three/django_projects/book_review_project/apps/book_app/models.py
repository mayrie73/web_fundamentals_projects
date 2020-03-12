# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models 
from ..login_registration_app.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author=models.ForeignKey(Author, related_name="books")
    user=models.ForeignKey(User,related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Review(models.Model):
    review= models.TextField(max_length=1000)
    rating= rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    user=models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)