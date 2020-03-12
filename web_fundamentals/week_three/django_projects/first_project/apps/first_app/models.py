# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=255,unique=True)
class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    name = models.DateField()