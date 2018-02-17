# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from product.models import Product

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    sale_price = DecimalField(max_digits=6, decimal_places=2)