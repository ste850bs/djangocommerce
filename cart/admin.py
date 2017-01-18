from django.contrib import admin
from cart.models import *


def get_kind(self):
	if self.composition:
		return "pronta consegna"
	else:
		return "40 giorni"

def get_customer(self):
	return self.user.username

def get_product(self):
	return self.product.name

def get_composition(self):
	if self.composition:
		return self.composition.name

def get_color(self):
	if self.color:
		return self.color.name

def get_scarpe(self):
	if self.scarpemisura:
		return self.scarpemisura.name

def get_cintura(self):
	if self.cintureLunghezza:
		return self.cintureLunghezza.name



class CartAdmin(admin.ModelAdmin):
	list_display = (get_kind, get_customer, get_product, get_composition, get_color, get_scarpe, get_cintura, 'quantity', 'price', 'pub_date')



admin.site.register(CartItem, CartAdmin)
