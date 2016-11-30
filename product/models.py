#!/usr/bin/env python

from __future__ import unicode_literals
from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils import timezone
#from product.forms import *
from django.utils.timezone import datetime

from django import forms

import django_filters


class Category(models.Model):
    title = models.CharField('titolo', max_length=100)
    title_uk = models.CharField('Titolo Inglese', max_length=250, null=True, blank=True)
    title_fr = models.CharField('Titolo Francese', max_length=250, null=True, blank=True)
    subtitle = models.CharField('sottotitolo', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categorie"




class Color(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Seleziona Categoria")
    name = models.CharField('nome colore', max_length=100)
    name_uk = models.CharField('nome colore Inglese', max_length=250, null=True, blank=True)
    name_fr = models.CharField('nome colore Francese', max_length=250, null=True, blank=True)
    code = models.CharField('codice colore', max_length=250, null=True, blank=True)
    css_color = models.CharField('css colore', max_length=250, null=True, blank=True)
    image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    thumb = ImageRatioField('image', '300x150', verbose_name="Miniatura: 300x150px")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Colori"
        ordering = ['name']




class Material(models.Model):
    name = models.CharField('nome colore', max_length=100)
    image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    description = models.TextField('descrizione', null=True, blank=True)
    thumb = ImageRatioField('image', '300x300', verbose_name="Miniatura")
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Metalli"




class TagliaScarpe(models.Model):
    name = models.CharField('nome', max_length=100)
    taglia = models.CharField('taglia', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Taglia Scarpe"




class CintureLunghezza(models.Model):
    name = models.CharField('nome', max_length=100)
    misure = models.CharField('taglia', max_length=250, null=True, blank=True)
    lunghezza = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lunghezza Cinture"




class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='marche')
    thumb = ImageRatioField('image', '312x135', verbose_name="Miniatura")

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:200px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produttore"




class Accessory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, verbose_name="Marca")
    designer = models.CharField(max_length=250, null=True, blank=True)
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='accessory', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    ## Composition
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiali")
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="Quantita")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    ## Delivery
    prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
    delivery = models.BooleanField('Consegna 40gg', default=False)

    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva', default=False)
    slide = models.BooleanField('Mostra in Slide', default=False)
    promo = models.BooleanField('Mostra in Promo', default=False)



    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessori"
        ordering = ['id']




class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    name_uk = models.CharField('Titolo Inglese', max_length=250, null=True, blank=True)
    name_fr = models.CharField('Titolo Francese', max_length=250, null=True, blank=True)
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    ## composizione
    #composition = models.ManyToManyField(Composition, null=True, blank=True, verbose_name="Composizioni")
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita",
                                    help_text = "quantita quando non e composizione")
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True,
                                help_text = "prezzo base")
    discount = models.IntegerField(blank=True, null=True, default= 0, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    ## Data
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori",
                                    help_text="solo se a 40 giorni")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Metallo", editable=False)
    scarpemisura = models.ManyToManyField(TagliaScarpe, null=True, blank=True, verbose_name="Taglia Scarpe", editable=False)
    cintureLunghezza = models.ManyToManyField(CintureLunghezza, null=True, blank=True, verbose_name="Lungheza Cinture", editable=False)
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name="larghezza")
    lenght = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name="lunghezza")
    depth = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name="Profondita")
    height = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    descrizione_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    descrizione_fr = models.TextField(null=True, blank=True, verbose_name="Descrizione Francese")
    ## Delivery
    prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
    delivery = models.BooleanField('Consegna 40gg', default=False)
    summer = models.BooleanField('Estate', default=False)
    winter = models.BooleanField('Winter', default=False)
    start_season = models.DateField('Inizio Stagione', blank=True, null=True)
    end_season = models.DateField('Fine Stagione', blank=True, null=True)
    ## Accessory
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published', editable=False)
    active = models.BooleanField('attiva', default=False)
    slide = models.BooleanField('Mostra in Slide', default=False)
    promo = models.BooleanField('Mostra in Promo', default=False)
    top_seller = models.BooleanField('Mostra in Piu Venduti', default=False)

    def save(self, *args, **kwargs):
        self.price_offer = self.price - (self.price * self.discount/100)
        self.pub_date = datetime.now()
        super(Product, self).save(*args, **kwargs) # Call the "real" save() method.

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Prodotti"
        ordering = ['id']




class Composition(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Prodotto")
    name = models.CharField(max_length=100, verbose_name="Titolo:", null=True, editable=False)
    name_uk = models.CharField(max_length=100, verbose_name="Titolo Inglese:", null=True, editable=False)
    name_fr = models.CharField(max_length=100, verbose_name="Titolo Francese:", null=True, editable=False)
    code = models.CharField('Codice', max_length=250, null=True, blank=True, editable=False)
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True, default= 0,
                                help_text = "maggiorazione di prezzo")
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    color = models.ForeignKey(Color, null=True, blank=True, verbose_name="Colori")
    material = models.ForeignKey(Material, null=True, blank=True, verbose_name="Metallo", editable=False)
    scarpemisura = models.ForeignKey(TagliaScarpe, null=True, blank=True, verbose_name="Taglia Scarpe",
                                    help_text = "lascia vuoto se non e scarpa")
    cintureLunghezza = models.ForeignKey(CintureLunghezza, null=True, blank=True, verbose_name="Lunghezza Cinture",
                                    help_text = "lascia vuoto se non e cintura")
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita")
    pub_date = models.DateTimeField('date published', editable=False)
    active = models.BooleanField('attiva', default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def save(self, *args, **kwargs):
        self.name = self.product.name + " - " + self.color.name
        self.name_uk = self.product.name_uk + " - " + self.color.name_uk
        self.name_fr = self.product.name_fr + " - " + self.color.name_fr
        self.code = self.product.id + self.color.id
        self.pub_date = datetime.now()
        super(Composition, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Composizioni"
        ordering = ['id']




## FILTER
class ProductFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['price', 'pub_date']




## forms
class ProductForm(forms.Form):
    product = Product.objects.first
    nome = forms.CharField(label='Nome', max_length=100)
    quantity = forms.IntegerField(label='Quantita')
    color = forms.ModelChoiceField(queryset=Color.objects.all().order_by('-id'))
    material = forms.ModelChoiceField(queryset=Material.objects.all().order_by('-id'))
    scarpemisura = forms.ModelChoiceField(queryset=TagliaScarpe.objects.all().order_by('-id'))
    cintureLunghezza = forms.ModelChoiceField(queryset=CintureLunghezza.objects.all().order_by('-id'))


