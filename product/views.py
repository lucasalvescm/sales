# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.

class ProductView(View):
    def get(self, request):
        template = 'product/products.html'
        products = Product.objects.all()
        return render(request, template, {'products':products})
