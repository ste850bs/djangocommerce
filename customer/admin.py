from django.contrib import admin
from customer.models import *
from django.forms import CheckboxSelectMultiple

#import nested_admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from django.contrib.auth.models import User


# Register your models here.

def get_username(self):
    return self.user.username


class UserAdmin(admin.ModelAdmin):
	pass

class CustomerAdmin(admin.ModelAdmin):
    list_display = (get_username, "discount", "active")
    model = User
    extra = 1
    fk_name = 'user'


admin.site.register(Customer, CustomerAdmin)
