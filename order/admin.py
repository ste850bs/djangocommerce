from django.contrib import admin
from django.contrib import admin
from order.models import *
from image_cropping import ImageCroppingMixin

# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class OrderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("id_user", "code", "name", "tot_price", "tot_discount", "prompt_delivery", "delivery", "confermato", "pagato", "spedito")


class OrderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_reserved", "prompt_delivery", "delivery")


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)