# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-07 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20160906_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, help_text='quantita quando non e composizione', null=True, verbose_name='quantita'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cintureLunghezza',
            field=models.ManyToManyField(blank=True, editable=False, null=True, to='product.CintureLunghezza', verbose_name='Lungheza Cinture'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, editable=False, null=True, to='product.Color', verbose_name='Seleziona Colori'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(blank=True, editable=False, null=True, to='product.Material', verbose_name='Seleziona Metallo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='scarpemisura',
            field=models.ManyToManyField(blank=True, editable=False, null=True, to='product.TagliaScarpe', verbose_name='Taglia Scarpe'),
        ),
    ]
