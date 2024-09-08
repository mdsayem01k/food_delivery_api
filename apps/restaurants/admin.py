
from .models import MenuItem, Restaurant,MenuCategory
from django.contrib import admin



class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'phone_number', 'email', 'town', 'country']

admin.site.register(Restaurant, RestaurantAdmin)

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'category', 'quantity', 'price', 'discount')
