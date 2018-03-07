# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Order

# Create your views here.


class OrderList(ListView):
    model = Order
    def get_queryset(self):
        queryset = Order.objects.filter(excluded=False)
        return queryset
class OrderCreate(SuccessMessageMixin,CreateView):
    model = Order
    success_message = "Venda criado com sucesso"
    success_url = reverse_lazy('order:orders')
    fields = ['product', 'client', 'quantity', 'description', 'sale_price']

class OrderUpdate(SuccessMessageMixin,UpdateView):
    model = Order
    success_message = "Venda atualizado com sucesso"
    success_url = reverse_lazy('order:orders')
    fields = ['product', 'client', 'quantity', 'description', 'sale_price']

class OrderDelete(View):
    def post(self,request):
        pk = request.POST.get('pk')
        # import ipdb; ipdb.set_trace()
        order = Order.objects.get(pk=pk)
        order.excluded = True
        order.save()
        context = {'mensagem':'Venda foi excluido'}  #  set your context
        return HttpResponse(context)
