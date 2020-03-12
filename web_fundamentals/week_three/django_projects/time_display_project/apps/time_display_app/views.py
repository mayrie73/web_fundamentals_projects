from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect

import datetime


  # the index function is called when root is visited
def index(request):
    context ={
        "current_time":datetime.datetime.now()
    }
   
    return render(request,"time_display_app/index.html", context)
