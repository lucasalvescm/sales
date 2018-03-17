# -*- coding: utf-8 -*-

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    delivered = forms.ChoiceField(label='Entregue?',required=False, widget=forms.CheckboxInput, choices=((True, 'Sim'), (False, 'Não')))
    canceled = forms.ChoiceField(label='Cancelado?',required=False, widget=forms.CheckboxInput, choices=((True, 'Sim'), (False, 'Não')))
    class Meta:
        model = Order
        fields = ['product', 'client', 'quantity', 'description', 'sale_price','delivered', 'canceled']