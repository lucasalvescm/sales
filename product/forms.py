# -*- coding: utf-8 -*-

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sale_price', 'cost_price', 'description']
    def __init__(self,*args,**kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width:65%'
        self.fields['sale_price'].widget.attrs['style'] = 'width:30%'
        self.fields['cost_price'].widget.attrs['style'] = 'width:30%'
        self.fields['description'].widget.attrs['style'] = 'width:65%;height:20%'
        