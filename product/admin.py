from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin

#import nested_admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin




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
 
'''
class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active")   
'''
class AccessoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active") 


class CompositionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "name", "price", "active")
    fields = ('image', 'title', 'quantity')


class ColorAdmin(ImageCroppingMixin, admin.ModelAdmin):
	list_display = ("category", "name")


'''
class AuthorInline(admin.TabularInline):
    model = Product.composition.through
    verbose_name = u"Composition"
    verbose_name_plural = u"Composition"


class BookAdmin(admin.ModelAdmin):

    exclude = ("composition", )
    inlines = (
       AuthorInline,
    )'''


'''
class LevelOneInline(NestedStackedInline):
    model = Color
    extra = 1
    fk_name = 'category'

class TopLevelAdmin(NestedModelAdmin):
    model = Category
    inlines = [LevelOneInline]
'''
                   
class CompositionAssociactionAdmin(NestedStackedInline):
    model = Composition
    extra = 1
    fk_name = 'product'


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = Product
    inlines = [CompositionAssociactionAdmin]
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active")  


admin.site.register(Category, MyModelAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(TagliaScarpe, MyModelAdmin)
admin.site.register(CintureLunghezza, MyModelAdmin)
admin.site.register(Material, MyModelAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Composition, CompositionAdmin)

#admin.site.register(Product, BookAdmin)
#admin.site.register(Category, TopLevelAdmin)




