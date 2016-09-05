from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin


def get_category(self):
    return self.category.title

def get_product(self):
	return self.product.name

def get_color(self):
    return self.color.name

def get_material(self):
    return self.material.name
'''
def get_cinture_lunghezza(self):
	return self.cintureLunghezza.id
	'''
'''
def get_scarpe_misura(self):
	return self.scarpemisura.name'''


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active")


class CompositionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "name", "price", "active")


class ColorAdmin(ImageCroppingMixin, admin.ModelAdmin):
	list_display = ("category", "name")




admin.site.register(Category, MyModelAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(TagliaScarpe, MyModelAdmin)
admin.site.register(CintureLunghezza, MyModelAdmin)
admin.site.register(Material, MyModelAdmin)
admin.site.register(Accessory, ProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Composition, CompositionAdmin)



