# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by("id")
    context={
        "access_records":webpages_list
    }
    return render(request,'first_app/index.html', context)