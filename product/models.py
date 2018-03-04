# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Nome")
    cost_price = models.DecimalField(max_digits=6, decimal_places=2,null=True, verbose_name=u"Preço de Custo")
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Preço de Venda")
    description = models.TextField(verbose_name=u"Descrição",blank=True,null=False)
    excluded = models.BooleanField(default=False)
    excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
