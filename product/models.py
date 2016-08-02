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
from django import forms


class Category(models.Model):
    title = models.CharField('titolo', max_length=100)
    subtitle = models.CharField('sottotitolo', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categorie"




class Color(models.Model):
    name = models.CharField('nome colore', max_length=100)
    code = models.CharField('codice colore', max_length=250, null=True, blank=True)
    css_color = models.CharField('css colore', max_length=250, null=True, blank=True)
    image = image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Colori"




class Material(models.Model):
    name = models.CharField('nome colore', max_length=100)
    image = image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    description = models.TextField('descrizione', null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Materiali"




class Shape(models.Model):
    name = models.CharField('nome colore', max_length=100)
    image = image = models.ImageField('immagine colore', blank=True, null=True, upload_to='color')
    description = models.TextField('descrizione', null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Forme"




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
    quantity = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    descrizione = models.TextField(null=True, blank=True, verbose_name="MATERIALE/FINITURA/COLORE")
    ## Delivery
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
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, verbose_name="Marca")
    designer = models.CharField(max_length=250, null=True, blank=True)
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    ## Composition
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiali")
    shape = models.ManyToManyField(Shape, null=True, blank=True, verbose_name="Seleziona Materiali")
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="MATERIALE/FINITURA/COLORE")
    ## Delivery
    prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
    delivery = models.BooleanField('Consegna 40gg', default=False)
    ## Accessory
    material = models.ManyToManyField(Accessory, null=True, blank=True, verbose_name="Accessori")

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
        verbose_name_plural = "Prodotti"
        ordering = ['id']




class Composition(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo:")
    code = models.CharField('Codice', max_length=250, null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="Seleziona Categorie")
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, verbose_name="Marca")
    designer = models.CharField(max_length=250, null=True, blank=True)

    ##
    ## Components
    component = models.ManyToManyField(Product, null=True, blank=True, verbose_name="Componenti")
    ##PRICE
    price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    price_offer = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
    ##MULTIMEDIA
    image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
    slider = ImageRatioField('image', '1170x600', verbose_name="Slider")
    thumb = ImageRatioField('image', '800x578', verbose_name="Miniatura")
    thumbdue = ImageRatioField('image', '745x558', verbose_name="Miniatura pagina dettaglio")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    ## Composition
    color = models.ManyToManyField(Color, null=True, blank=True, verbose_name="Seleziona Colori")
    material = models.ManyToManyField(Material, null=True, blank=True, verbose_name="Seleziona Materiali")
    ## Data
    quantity = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    size = models.CharField('Misure', max_length=250, null=True, blank=True)
    width = models.IntegerField(blank=True, null=True, verbose_name="larghezza")
    lenght = models.IntegerField(blank=True, null=True, verbose_name="lunghezza")
    depth = models.IntegerField(blank=True, null=True, verbose_name="Profondita")
    height = models.IntegerField(blank=True, null=True, verbose_name="altezza")
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=2, blank=True, null=True)
    models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    descrizione = models.TextField(null=True, blank=True, verbose_name="MATERIALE/FINITURA/COLORE")
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
        verbose_name_plural = "Composizioni"
        ordering = ['id']



