# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def service_worker(request):
    return render(request, '/core/static/OneSignalSDKUpdaterWorker.js', {'foo':'bar'},
                        content_type="application/x-javascript")


def manifest(request):
    
    return render(request, 'notification/manifest.json',
                        content_type="application/json")