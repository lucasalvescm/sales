# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from order.models import Order
from client.models import Client

class Dashboard(LoginRequiredMixin,View):
    def get(self, request):
        template = 'adm/dashboard.html'
        context = self._get_values()
        return render(request, template, context)

    def _get_values(self, *args, **kwargs):
    	start_date = datetime.datetime.now() + datetime.timedelta(-30)
    	end_date = datetime.datetime.now()
    	orders = Order.objects.filter(order_date__range=(start_date,end_date)).values('sale_price')
    	clients = Client.objects.all().values('pk')
    	total_sold = 0.0
    	total_sales = len(orders)
    	for order in orders:
    		total_sold += float(order['sale_price'])
    	orders_not_delivered = len(orders.filter(delivered=False))
    	data = {
    		'total_sold': str(total_sold).replace('.',','),
    		'total_sales': total_sales,
    		'total_clients': len(clients),
    		'orders_not_delivered': orders_not_delivered,
    		'start_date': start_date.strftime('%d-%m-%Y'),
    		'end_date': end_date.strftime('%d-%m-%Y')
    	}
    	return data





