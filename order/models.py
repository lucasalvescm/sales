# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from product.models import Product

from datetime import datetime

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Nome")
    cellphone = models.CharField(max_length=17, blank=True, verbose_name=u"Telefone")
    email = models.CharField(max_length=100,null=True)
    excluded = models.BooleanField(default=False)
    excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product)
    client = models.ForeignKey(Client)
    quantity = models.IntegerField()
    description = models.TextField(null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    delivered = models.BooleanField(default=False)
    canceled = models.BooleanField(default=True)
    order_date = models.DateTimeField(default=datetime.now())
    delivered_date = models.DateTimeField(default=datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.product,self.client)