from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import authenticate, login
from django.core import validators
from django.contrib import messages
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_input(self, post_data):
        errors = []
        if User.objects.filter(email=post_data["email"]).exists():
            errors.append("Invalid, Email already exists!")
        if len(post_data["first_name"]) < 2:
            errors.append("First name should be more than 2 characters")
        if len(post_data["last_name"]) < 2:
            errors.append("Last name should be more than 2 characters")
        if not post_data['first_name'].isalpha():
            errors.append("First name should only contain letters")
        if not post_data['last_name'].isalpha():
            errors.append("Last name should only contain letters")
        if not EMAIL_REGEX.match(post_data['email']):
            errors.append("You must enter a valid email!")
        if len(post_data["email"]) < 0:
            errors.append("Email field cannot be blank. Please enter a Valid Email Address")
        if len(post_data["password"]) < 8:
            errors.append("Password must be at least 8 characters!")
        if (post_data["password"]) != (post_data["password_confirmation"]):
            errors.append("Password does not match password confirmation.")
        return errors
    def validate_login(self, post_data):
        errors= []
        user = (User.objects.filter(email=post_data['email']))[0]
        hashed_password = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        if (User.objects.filter(email=post_data['email']).exists())!= (["user.email"]) >0:
            errors.append("invalid email")
        if (bcrypt.checkpw(post_data["password"].encode(), user.password.encode()))== 0:
            errors.append("invalid password")
            return errors   
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


