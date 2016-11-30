# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-05 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20160905_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.AddField(
            model_name='composition',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Prodotto'),
        ),
    ]
