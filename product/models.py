# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
