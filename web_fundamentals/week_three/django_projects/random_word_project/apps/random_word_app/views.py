# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    context ={
        "random_word":get_random_string()
    }
    return render(request,"random_word_app/index.html", context)
def create(request):
    print " GOT TO CREATE ROUTE"
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['random_word'] = get_random_string(length = 14)
        request.session['counter'] += 1
    # return render(request, 'random_word_app/index.html')
    return redirect('/')
def reset(request):
    request.session['counter'] = 0
    return redirect('/')
   
