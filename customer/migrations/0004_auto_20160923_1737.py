# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-23 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_fatturazione_indirizzospedizione'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatturazione',
            name='pub_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='indirizzospedizione',
            name='pub_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='date published'),
        ),
    ]
