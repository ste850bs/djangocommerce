# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-06 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20160906_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='cintureLunghezza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.CintureLunghezza', verbose_name='Cinture'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Color', verbose_name='Colori'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Material', verbose_name='Metallo'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='scarpemisura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.TagliaScarpe', verbose_name='Scarpe'),
        ),
    ]
