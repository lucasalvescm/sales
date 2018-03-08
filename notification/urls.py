from django.conf.urls import url,include
from django.contrib import admin
from .views import worker,manifest,updater_workder

urlpatterns = [
    url('^OneSignalSDKUpdaterWorker.js$', updater_workder),
    url('^OneSignalSDKWorker.js$', worker),
    url('^manifest.json$', manifest)
]