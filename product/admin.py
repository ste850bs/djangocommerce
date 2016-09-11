from django.contrib import admin
from product.models import *
from image_cropping import ImageCroppingMixin
from django.forms import CheckboxSelectMultiple

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



class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
 

class AccessoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active") 


class CompositionAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("code", "image_img", "name", "price", "active")
    #fields = ('image', 'name', 'quantity')


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
    fields = ('image', ('color', 'scarpemisura', 'cintureLunghezza'), ('quantity', 'price'))


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #duplicate function
    def duplicate_event(ModelAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate_event.short_description = "Duplica Record Selezionati"

    model = Product
    inlines = [CompositionAssociactionAdmin]
    list_display = ("image_img", "code", "name", "price", "discount", "price_offer", "prompt_delivery", "delivery", "promo", "active")
    list_editable = ('active',)
    fields = (
                ("name", "code"),
                "category", 
                ("price", "discount"),
                "quantity",
                "color",
                #("color", "material"),
                #("scarpemisura", "cintureLunghezza"),
                "size",
                ("width", "lenght", "depth", "height"),
                "volume",
                "descrizione", "album",
                "image", "slider", "thumb", "thumbdue", "croplibero",
                ("prompt_delivery", "delivery"),
                ("slide", "promo"),
                "tags", "active", "pub_date"
            )

    actions = ['duplicate_event']





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




