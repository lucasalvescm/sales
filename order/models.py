# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from product.models import Product

from datetime import datetime

from client.models import Client

# Create your models here.

# class Client(models.Model):
#     name = models.CharField(max_length=200, verbose_name=u"Nome")
#     cellphone = models.CharField(max_length=17, blank=True, verbose_name=u"Telefone")
#     email = models.CharField(max_length=100,null=True)
#     excluded = models.BooleanField(default=False)
#     excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name=u"Produto")
    client = models.ForeignKey(Client, verbose_name=u"Cliente")
    quantity = models.IntegerField(verbose_name=u"Quantidade")
    description = models.TextField(null=True, verbose_name=u"Descrição")
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Preço de Venda")
    delivered = models.BooleanField(default=False, verbose_name=u"Entregue")
    canceled = models.BooleanField(default=True, verbose_name=u"Cancelado")
    order_date = models.DateTimeField(default=datetime.now(), verbose_name=u"Data do Pedido")
    delivered_date = models.DateTimeField(default=datetime.now(), verbose_name=u"Data de Entrega")
    excluded = models.BooleanField(default=False)
    excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.product,self.client)