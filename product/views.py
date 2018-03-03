# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Product
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class ProductList(ListView):
    model = Product

class ProductCreate(SuccessMessageMixin,CreateView):
    model = Product
    success_message = "Produto criado com sucesso"
    success_url = reverse_lazy('product:products')
    fields = ['name', 'sale_price', 'cost_price', 'description']

class ProductUpdate(SuccessMessageMixin,UpdateView):
    model = Product
    success_message = "Produto atualizado com sucesso"
    success_url = reverse_lazy('product:products')
    fields = ['name', 'sale_price', 'cost_price', 'description']

class ProductDelete(View):
    def post():
        import ipdb; ipdb.set_trace()


    

        
