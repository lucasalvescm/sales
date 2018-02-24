# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Dashboard(View):
    def get(self, request):
        template = 'adm/dashboard.html'
        return render(request, template, {})