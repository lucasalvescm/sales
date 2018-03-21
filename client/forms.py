# -*- coding: utf-8 -*-

from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'cellphone', 'email']
    def __init__(self,*args,**kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width:65%'
        self.fields['cellphone'].widget.attrs['style'] = 'width:65%'
        self.fields['email'].widget.attrs['style'] = 'width:20%'
        