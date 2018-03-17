# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderForm

# Create your views here.


class OrderList(LoginRequiredMixin,ListView):
    model = Order
    def get_queryset(self):
        queryset = Order.objects.filter(excluded=False)
        return queryset
class OrderCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Order
    form_class = OrderForm
    success_message = "Venda criado com sucesso"
    success_url = reverse_lazy('order:orders')
    
class OrderUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Order
    success_message = "Venda atualizado com sucesso"
    success_url = reverse_lazy('order:orders')
    fields = ['product', 'client', 'quantity', 'description', 'sale_price']

class OrderDelete(LoginRequiredMixin,DeleteView):
    model = Order
    success_message = "Venda excluída com sucesso"
    success_url = reverse_lazy('order:orders')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    # def post(self,request):
    #     pk = request.POST.get('pk')
    #     # import ipdb; ipdb.set_trace()
    #     order = Order.objects.get(pk=pk)
    #     order.excluded = True
    #     order.save()
    #     context = {'mensagem':'Venda foi excluido'}  #  set your context
    #     return HttpResponse(context)
