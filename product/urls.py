"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    url(r'^$', ProductList.as_view(),name='products'),
    url(r'novo$', ProductCreate.as_view(),name='product_new'),
    url(r'editar/(?P<pk>\d+)$', ProductUpdate.as_view(),name='product_update'),
    url(r'excluir/(?P<pk>\d+)$', ProductDelete.as_view(), name='product_delete'),
]
