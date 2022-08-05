from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import *

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email','name','mobile', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email','mobile', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile', 'password1', 'password2', 'tc'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ['user', 'gender', 'locality', 'city', 'address','pin','state','profile_image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'name', 'locality', 'city','pin','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'selling_price', 'discounted_price', 'description','brand','category', 'product_image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'customer', 'product', 'quantity','ordered_data','status']


