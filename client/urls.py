from django.conf.urls import url,include
from django.contrib import admin
from .views import ClientList, ClientCreate, ClientDelete, ClientUpdate 

urlpatterns = [
    url(r'^$', ClientList.as_view(),name='clients'),
    url(r'novo$', ClientCreate.as_view(),name='client_new'),
    url(r'editar/(?P<pk>\d+)$', ClientUpdate.as_view(),name='client_update'),
    url(r'excluir$', ClientDelete.as_view(), name='client_delete')

]