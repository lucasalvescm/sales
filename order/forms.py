# -*- coding: utf-8 -*-

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    delivered = forms.ChoiceField(label='Entregue?',required=False, widget=forms.CheckboxInput, choices=((True, 'Sim'), (False, 'Não')))
    canceled = forms.ChoiceField(label='Cancelado?',required=False, widget=forms.CheckboxInput, choices=((True, 'Sim'), (False, 'Não')))
    class Meta:
        model = Order
        fields = ['product', 'client', 'quantity', 'description', 'sale_price','delivered', 'canceled']
    def __init__(self,*args,**kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['style'] = 'width:65%'
        self.fields['client'].widget.attrs['style'] = 'width:65%'
        self.fields['quantity'].widget.attrs['style'] = 'width:20%'
        self.fields['sale_price'].widget.attrs['style'] = 'width:30%'
        self.fields['client'].widget.attrs['style'] = 'width:65%'
        self.fields['description'].widget.attrs['style'] = 'width:65%;height:20%'