# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Client

# Create your views here.


class ClientList(ListView):
    model = Client
    def get_queryset(self):
        queryset = Client.objects.filter(excluded=False)
        return queryset
class ClientCreate(SuccessMessageMixin,CreateView):
    model = Client
    success_message = "Cliente criado com sucesso"
    success_url = reverse_lazy('product:products')
    fields = ['name', 'cellphone', 'email']

class ClientUpdate(SuccessMessageMixin,UpdateView):
    model = Client
    success_message = "Cliente atualizado com sucesso"
    success_url = reverse_lazy('product:products')
    fields = ['name', 'cellphone', 'email']

class ClientDelete(View):
    def post(self,request):
        pk = request.POST.get('pk')
        # import ipdb; ipdb.set_trace()
        client = Client.objects.get(pk=pk)
        client.excluded = True
        client.save()
        context = {'mensagem':'Cliente foi excluido'}  #  set your context
        return HttpResponse(context)
