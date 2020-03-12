from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import datetime
# Create your views here.
def index(request):
    print "HOORAY GOT TO THE INDEX ROUTE"
    if not 'name' in request.session:
        request.session['name'] = "test"
    if not 'location' in request.session:
        request.session['location'] = "test"
    if not 'language' in request.session:
        request.session['language'] = "test"
    if not 'comment' in request.session:
        request.session['comment'] = "test"
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request,'survey_form_app/index.html')
def process(request):
    print "HOORAY GOT TO CREATE ROUTE" 
    request.session['count'] +=1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language']= request.POST['language']
    request.session['comment']= request.POST['comment'] 

    return redirect('/result')

def result(request):
    print "HOORAY GOT TO RESULT ROUTE" 
    return render(request,'survey_form_app/result.html')
def refresh(request):
    print "HOORAY GOT TO REFRESH ROUTE" 
    return redirect('/')