# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-06 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160905_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.CharField(blank=True, editable=False, max_length=250, null=True, verbose_name='Codice'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='name',
            field=models.CharField(editable=False, max_length=100, verbose_name='Titolo:'),
        ),
    ]
