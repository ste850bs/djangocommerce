from django.contrib import admin
from sito.models import *
from image_cropping import ImageCroppingMixin


def get_category(self):
    return self.category.title


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "name", "active")




admin.site.register(Slider, SliderAdmin)

