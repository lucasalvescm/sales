# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Client, Order

# Create your views here.


class ClientList(ListView):
    # def get(self, request):
    #     template = 'order/clients.html'
    #     clients = Client.objects.all()
    #     return render(request, template, {'clients':clients})
    model = Client

class OrderList(ListView):
    # def get(self, request):
    #     template = 'order/orders.html'
    #     orders = Order.objects.all()
    #     return render(request, template, {'orders':orders})
    model = Order
