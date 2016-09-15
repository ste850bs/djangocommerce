from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince
from django.utils import timezone
from product.models import *

from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm




class CartItem(models.Model):
	codice = models.CharField(max_length=100, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True, verbose_name="Utente")
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
		self.price_total = self.price * self.quantity
		self.price_discount = self.price_total - (self.price_total * self.product.discount/100)
		self.price_reserved = self.price_discount - (self.price_discount * self.user.customer.discount/100)
		super(CartItem, self).save(*args, **kwargs) # Call the "real" save() method.

	def __unicode__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = "Articoli Carrello"
		ordering = ['id']



class AddForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['user', 'product', 'color', 'cintureLunghezza', 'scarpemisura', 'composition', 'price', 'quantity']


