# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class Client(View):
    def get(self, request):
        template = 'order/clients.html'
        return render(request, template, {})

class Order(View):
    def get(self, request):
        template = 'order/orders.html'
        return render(request, template, {})
