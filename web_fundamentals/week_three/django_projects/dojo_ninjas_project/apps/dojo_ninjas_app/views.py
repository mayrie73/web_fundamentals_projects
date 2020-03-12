from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import datetime
# Create your views here.
def index(request):
    print "Hello Got to Index Route"
    return render(request,"dojo_ninjas_app/index.html")

