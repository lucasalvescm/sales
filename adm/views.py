# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(LoginRequiredMixin,View):
    def get(self, request):
        template = 'adm/dashboard.html'
        return render(request, template, {})