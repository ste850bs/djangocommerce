# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160829_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='album',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='category',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='component',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='price_offer',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='promo',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='prompt_delivery',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='slide',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='accessory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cintureLunghezza',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='scarpemisura',
        ),
        migrations.AddField(
            model_name='composition',
            name='cintureLunghezza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.CintureLunghezza', verbose_name='Lungheza Cinture'),
        ),
        migrations.AddField(
            model_name='composition',
            name='scarpemisura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.TagliaScarpe', verbose_name='Taglia Scarpe'),
        ),
        migrations.AddField(
            model_name='material',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prezzo'),
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.ManyToManyField(blank=True, null=True, to='product.Composition', verbose_name='Composizioni'),
        ),
        migrations.RemoveField(
            model_name='composition',
            name='color',
        ),
        migrations.AddField(
            model_name='composition',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Color', verbose_name='Seleziona Colori'),
        ),
        migrations.RemoveField(
            model_name='composition',
            name='material',
        ),
        migrations.AddField(
            model_name='composition',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Material', verbose_name='Seleziona Metallo'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='quantita'),
        ),
    ]
