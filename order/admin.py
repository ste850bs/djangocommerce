from django.contrib import admin
from order.models import *
from image_cropping import ImageCroppingMixin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass



class OrderListItemAdmin(NestedStackedInline):
    model = OrderItem
    extra = 2
    fk_name = 'order'
    list_display = ("quantity", "price", "price_total", "price_discount", "price_reserved")
    fields = (
        ("order", "product", "composition", "quantity"),
        ("price_total", "price_discount", "price_reserved")
        )



class OrderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("user", "code", "tot_price", "tot_discount", "tot_price_reserved", "inlavorazione", "pagato", "spedito", "chiuso")
    list_editable=("inlavorazione", "pagato", "spedito", "chiuso")
    fields = (
        ("user", "code"),
        ("tot_price", "tot_discount", "tot_price_reserved"),
        ("inlavorazione", "pagato", "spedito", "chiuso")
        )
    model = Order
    inlines = [OrderListItemAdmin]

    
class OrderItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("quantity", "price", "price_total", "price_discount", "price_reserved")


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
