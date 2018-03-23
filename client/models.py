# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Nome")
    cellphone = models.CharField(max_length=17, null=True, blank=True, verbose_name=u"Telefone")
    email = models.CharField(max_length=100, null=True, blank=True)
    excluded = models.BooleanField(default=False)
    excluded_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
