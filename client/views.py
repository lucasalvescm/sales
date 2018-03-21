# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client
from .forms import ClientForm

# Create your views here.


class ClientList(LoginRequiredMixin,ListView):
    model = Client
    def get_queryset(self):
        queryset = Client.objects.filter(excluded=False)
        return queryset
class ClientCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Client
    form_class = ClientForm
    success_message = "Cliente criado com sucesso"
    success_url = reverse_lazy('client:clients')

class ClientUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Client
    form_class = ClientForm
    success_message = "Cliente atualizado com sucesso"
    success_url = reverse_lazy('client:clients')

class ClientDelete(LoginRequiredMixin,DeleteView):
    model = Client
    success_url = reverse_lazy('client:clients')
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    # def post(self,request):
    #     pk = request.POST.get('pk')
    #     # import ipdb; ipdb.set_trace()
    #     client = Client.objects.get(pk=pk)
    #     client.excluded = True
    #     client.save()
    #     context = {'mensagem':'Cliente foi excluido'}  #  set your context
    #     return HttpResponse(context)
