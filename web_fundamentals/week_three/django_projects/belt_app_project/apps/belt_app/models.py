# Create your models here.
from __future__ import unicode_literals
from django.db import models
from ..login_registration_app.models import User
# Create your models here.

class ProductManager(models.Manager):
    def validate_input(self, post_data):
        errors = []  
        if len(post_data["item"]) < 0:
            errors.append("Item cannot be empty")
        if len(post_data["item"]) < 3:
            errors.append("Item name must be more than 3 characters")
        return errors
class Product(models.Model):
    item = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="products_created")
    liked_users=models.ManyToManyField(User,related_name="products_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
