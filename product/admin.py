from django.contrib import admin
from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin

def get_category(self):
    return self.categoria.titolo

'''
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", "active", "azienda")
'''
