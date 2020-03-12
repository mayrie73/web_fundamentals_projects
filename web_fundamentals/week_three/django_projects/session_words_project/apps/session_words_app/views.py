# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
def index(request):
    if not 'word' in request.session:
        request.session['word'] = "test"
    if not 'color' in request.session:
        request.session['color'] = "test"
    if not 'font' in request.session:
        request.session['font'] = "p"
    if not 'queue' in request.session:
        request.session['queue'] = []
    return render(request,'session_words_app/index.html')
def process(request):
    request.session["word"] = request.POST["word"]
    request.session["color"] = request.POST["color"]
    print 'here'
    if request.POST['font'] == "bold":
        print "true"
        request.session["font"] = True
    else:
        print "false"
        request.session["font"] = False    
    context = {"font": request.session['font']}
         dic= {"word": request.session["word"],
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
            "color": request.session["color"],
            "font": request.session['font']
    }
    temp = request.session['queue']
    temp.append(dic)
    request.session['queue'] = temp
    return redirect('/')
def refresh(request):
    request.session['queue'] = []
    return redirect('/')

