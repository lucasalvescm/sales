# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from .models import Product
from django.views.generic import DetailView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ProductList(ListView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    # success_url = reverse_lazy('products')
    fields = ['name', 'sale_price', 'cost_price', 'description']
