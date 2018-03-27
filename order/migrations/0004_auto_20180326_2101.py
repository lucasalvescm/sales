# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 00:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180323_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_form',
            field=models.IntegerField(blank=True, choices=[(1, 'Cartão de Crédito'), (2, 'Cartão de Débito'), (3, 'Dinheiro')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 0, 1, 57, 220473, tzinfo=utc), verbose_name='Data de Entrega'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 0, 1, 57, 220473, tzinfo=utc), verbose_name='Data do Pedido'),
        ),
    ]