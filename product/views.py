# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Product
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ProductList(LoginRequiredMixin,ListView):
    model = Product
    def get_queryset(self):
        queryset = Product.objects.filter(excluded=False)
        return queryset

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
    def post(self,request):
        pk = request.POST.get('pk')
        product = Product.objects.get(pk=pk)
        product.excluded = True
        product.save()
        context = {'mensagem':'Produto foi excluido'}  #  set your context
        return HttpResponse(context)

    

        
