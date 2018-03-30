# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from product.models import Product

from datetime import datetime

from client.models import Client

from .utils import CHOICES_PAYMENT

class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name=u"Produto")
    client = models.ForeignKey(Client, verbose_name=u"Cliente")
    quantity = models.IntegerField(verbose_name=u"Quantidade")
    description = models.TextField(null=True, blank=True, verbose_name=u"Descrição")
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Preço de Venda (R$)")
    delivered = models.BooleanField(default=False, blank=True, verbose_name=u"Entregue")
    canceled = models.BooleanField(default=True, blank=True, verbose_name=u"Cancelado")
    order_date = models.DateTimeField(default=timezone.now, verbose_name=u"Data do Pedido")
    delivered_date = models.DateTimeField(default=timezone.now, verbose_name=u"Data de Entrega")
    payment_form = models.IntegerField(choices=CHOICES_PAYMENT, null=True, blank=True, verbose_name=u"Forma de pagamento")
    paid_out = models.BooleanField(default=False)
    excluded = models.BooleanField(default=False)
    excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.product,self.client)