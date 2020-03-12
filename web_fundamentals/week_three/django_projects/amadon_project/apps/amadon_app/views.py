# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    request.session['purchase'] = []
    return render(request, 'amadon_app/index.html')

def process(request):
    purchase = {}
    for key, value in request.POST.items():
        if key!="csrfmiddlewaretoken":
            purchase[key] = value

    if purchase['product_id'] == '12':
        purchase['product'] = 'Shoes'
        purchase['total'] = int(purchase['quantity'])*120.00
    elif purchase['product_id'] == '13':
        purchase['product'] = 'Make-Up'
        purchase['total'] = int(purchase['quantity'])*10.00
    elif purchase['product_id'] == '14':
        purchase['product'] = 'Utensils'
        purchase['total'] = int(purchase['quantity'])*30.00
    else:
        purchase['product'] = 'Books'
        purchase['total'] = int(purchase['quantity'])*50.00

    request.session['purchase'] = []
    request.session['purchase'] = purchase
    
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')
