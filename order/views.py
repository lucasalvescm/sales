# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView

from .models import Client, Order

# Create your views here.


class ClientView(View):
    def get(self, request):
        template = 'order/clients.html'
        clients = Client.objects.all()
        return render(request, template, {'clients':clients})

class OrderView(View):
    def get(self, request):
        template = 'order/orders.html'
        orders = Order.objects.all()
        return render(request, template, {'orders':orders})
