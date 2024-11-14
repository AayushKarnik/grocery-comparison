from django.contrib import admin
from .models import Store, Product, Price, UserPreference

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_url', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'availability_date', 'location')
    search_fields = ('product__name', 'store__name')
    list_filter = ('store', 'location', 'availability_date')
    date_hierarchy = 'availability_date'

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_location', 'max_price', 'categories')
    search_fields = ('user__username', 'preferred_location')
    list_filter = ('preferred_location',)

class PriceInline(admin.TabularInline):
    model = Price
    extra = 1  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    inlines = [PriceInline]  # Adds an inline form for prices
