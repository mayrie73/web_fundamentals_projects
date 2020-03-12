# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import authenticate, login
from django.core import validators
from django.contrib import messages
# Create your models here.
class CourseManager(models.Manager):
    def validate_input(self, post_data):
        errors = []
        if len(post_data["name"])< 5:
            errors.append("Name should be more than 5 characters")
        if len(post_data["description"])< 15:
            errors.append("Description should be more than 15 characters") 
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    objects=CourseManager()
   