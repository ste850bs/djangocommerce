# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-06 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_composition_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='name',
            field=models.CharField(editable=False, max_length=100, null=True, verbose_name='Titolo:'),
        ),
    ]
