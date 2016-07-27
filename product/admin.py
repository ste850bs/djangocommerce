from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin


def get_category(self):
    return self.category.title


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active")




admin.site.register(Category, MyModelAdmin)
admin.site.register(Color, MyModelAdmin)
admin.site.register(Material, MyModelAdmin)
admin.site.register(Accessory, ProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Composition, ProductAdmin)



