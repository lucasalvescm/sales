# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def worker(request):
    return render(request, 'notification/OneSignalSDKWorker.js',
                        content_type="application/x-javascript")

def updater_workder(request):
    return render(request, 'notification/OneSignalSDKUpdaterWorker.js',
                        content_type="application/x-javascript")

def manifest(request):
    
    return render(request, 'notification/manifest.json',
                        content_type="application/json")