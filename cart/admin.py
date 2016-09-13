from django.contrib import admin
from cart.models import *


class CartAdmin(admin.ModelAdmin):
	pass

admin.site.register(CartItem, CartAdmin)
