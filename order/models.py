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

from django import forms



class Order(models.Model):
	id_user = models.CharField('id utente', max_length=250, null=True, blank=True)
	name = models.CharField(max_length=100, verbose_name="Titolo:")
	code = models.CharField('Codice', max_length=250, null=True, blank=True)
	tot_price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	tot_discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
	price_reserved = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
	prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
	delivery = models.BooleanField('Consegna 40gg', default=False)
	pub_date = models.DateTimeField('date published')
	confermato = models.BooleanField('confermato', default=False)
	pagato = models.BooleanField('pagato', default=False)
	spedito = models.BooleanField('spedito', default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Ordine"
		ordering = ['id']




class OrderItem(models.Model):
	id_ordine = models.CharField('id ordine', max_length=250, null=True, blank=True)
	name = models.CharField(max_length=100, verbose_name="Titolo:")
	code = models.CharField('Codice', max_length=250, null=True, blank=True)
	designer = models.CharField(max_length=250, null=True, blank=True)
	price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
	price_reserved = models.DecimalField('Prezzo Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to='product', verbose_name="Immagine")
	croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
	album = FilerFolderField(null=True, blank=True)
	prompt_delivery = models.BooleanField('Pronta Consegna', default=False)
	delivery = models.BooleanField('Consegna 40gg', default=False)
	pub_date = models.DateTimeField('date published')

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
		verbose_name_plural = "Prodotti Ordinati"
		ordering = ['id']
