from django.contrib import admin
from order.models import *
from image_cropping import ImageCroppingMixin

# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class OrderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("user", "code", "tot_price", "tot_discount", "inlavorazione", "pagato", "spedito", "chiuso")


class OrderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("quantity", "price", "price_total", "price_discount", "price_reserved")


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)