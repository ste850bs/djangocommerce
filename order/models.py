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
from product.models import *
from customer.models import *
from cart.models import *
from order.models import *


from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm



class Order(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, verbose_name="Utente")
	code = models.CharField('Codice', max_length=250, null=True, blank=True)
	tot_price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True, default=0)
	tot_discount = models.DecimalField('Totale Scontato', max_digits=10, decimal_places=2, blank=True, null=True)
	tot_price_reserved = models.DecimalField('Prezzo Scontato Riservato', max_digits=10, decimal_places=2, blank=True, null=True)
	pub_date = models.DateTimeField('date published', editable=False)
	inlavorazione = models.BooleanField('in lavorazione', default=False)
	pagato = models.BooleanField('pagato', default=False)
	spedito = models.BooleanField('spedito', default=False)
	chiuso = models.BooleanField('chiuso', default=False)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		super(Order, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.pub_date.strftime('%Y-%m-%d')

	class Meta:
		verbose_name_plural = "Ordine"
		ordering = ['id']




class OrderItem(models.Model):
	order = models.ForeignKey(Order, null=True, blank=True, verbose_name="Ordine")
	product = models.ForeignKey(Product, null=True, blank=True, verbose_name="Prodotto")
	composition = models.ForeignKey(Composition, null=True, blank=True, verbose_name="Composizione")
	color = models.ForeignKey(Color, null=True, blank=True, verbose_name="Colore")
	cintureLunghezza = models.ForeignKey(CintureLunghezza, null=True, blank=True, verbose_name="Lunghezza Cinture")
	scarpemisura = models.ForeignKey(TagliaScarpe, null=True, blank=True, verbose_name="Misura scarpe")
	#prezzo
	price = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	price_total = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	price_discount = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	price_reserved = models.DecimalField('Prezzo', max_digits=10, decimal_places=2, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True, verbose_name="quantita")
	pub_date = models.DateTimeField('date published', editable=False)

	def save(self, *args, **kwargs):
		self.pub_date = datetime.now()
		#se lo faccio calcolare in front con js non ce bisogno di questo if (tieni solo calcolo in else)
		if self.composition:
			self.price_total = (self.price + self.composition.price) * self.quantity ####
		else:
			self.price_total = self.price * self.quantity ## ok ok ok 
		self.price_discount = self.price_total - (self.price_total * self.product.discount/100)
		self.price_reserved = self.price_discount - (self.price_discount * self.order.user.profile.discount/100)
		super(OrderItem, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		#return self.pub_date.strftime('%Y-%m-%d')
		return self.product.code

	class Meta:
		verbose_name_plural = "Prodotti in Ordine"
		ordering = ['id']




class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'tot_price', 'tot_discount', 'tot_price_reserved']



class AddOrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = ['order', 'product', 'composition', 'color', 'cintureLunghezza', 'scarpemisura', 'price', 'price_total', 'price_discount', 'price_reserved']

