from django.conf.urls import url,include
from django.contrib import admin
from .views import service_worker,manifest

urlpatterns = [
    url('^serviceworker.js$', service_worker),
    url('^manifest.json$', manifest)
]